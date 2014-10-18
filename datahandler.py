# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys
# sys.path.append("..")
import re
import subprocess
from subprocess import call
from datetime import *
from common.cook import *
import time
import json
import tornado
import torndb

mysql_host = '127.0.0.1'
mysql_port = 3306
mysql_database = 'crosswalk'
mysql_user = 'root'
mysql_password = 'mysqlnightly'

enable_rcategory_insert = 1
enable_rcase_insert = 1

protocol = 'http'
host = 'wrt-qa-report.sh.intel.com'
path = 'api/reports'
auto_token = 'NL1sbHvpDadoM4jrml7A'
limit_amount = '40'
config = [protocol, host, path, auto_token, limit_amount]
url = '%s://%s/%s/?auto_token=%s&limit_amount=%s' % tuple(config)
filename = 'index.html?auto_token=' + \
    auto_token + '&limit_amount=' + limit_amount
dir = '/home/nightlytest/nightly_indicator/data'

def jsonToDB(file):
    fp = open(dir + '/' + file)
    reader = fp.read()
    d = json.loads(reader, strict=False)
    db = torndb.Connection(
        host=mysql_host, database=mysql_database,
        user=mysql_user, password=mysql_password)

    for var in d:
        qa_id = var['qa_id']
        build_id = var['build_id'].strip()
        profile = var['profile'].strip()
        testtype = var['testtype'].strip()
        ab = testtype.lower()
        branch = ''
        architecture = ''
        dic = {'Canary': '', 'canary': '', 'Beta': '', 'beta':
               '', 'Stable': '', 'stable': '', 'Tizen': '', 'tizen': ''}
        if ab.endswith('canary'):
            branch = 'Canary'
            architecture = multi_replace(testtype, dic).strip()
            print architecture
        elif ab.endswith('beta'):
            branch = 'Beta'
            architecture = multi_replace(testtype, dic).strip()
        elif ab.endswith('stable'):
            branch = 'Stable'
            architecture = multi_replace(testtype, dic).strip()
        else:
            branch = ''
            architecture = testtype.strip()
        hardware = var['hardware'].strip()
        deviceid = 0
        result_id = ''

        if hardware.lower().find('cordova') >= 0:
            hardware2 = hardware.replace('Nightly Cordova', '').strip()
            hardware = hardware.replace(hardware2, '').strip()
            print hardware2 + '****** cordova ******'
            try:
                result_id = db.query(
                    'SELECT DISTINCT * FROM crosswalk.device WHERE name=%s', hardware2)
                deviceid = result_id[0].id
            except Exception, ex:
                print ex
        elif hardware.lower().find('webdriver ') >= 0:
            hardware2 = hardware.replace('Nightly WebDriver', '').strip()
            hardware = hardware.replace(hardware2, '').strip()
            print hardware2 + '****** webdriver ******'
            try:
                result_id = db.query(
                    'SELECT DISTINCT * FROM crosswalk.device WHERE name=%s', hardware2)
                deviceid = result_id[0].id
            except Exception, ex:
                print ex
        elif hardware.lower().find('nightly ') >= 0:
            hardware2 = hardware.replace('Nightly', '').strip()
            hardware = hardware.replace(hardware2, '').strip()
            print hardware2 + '$'
            try:
                result_id = db.query(
                    'SELECT DISTINCT * FROM crosswalk.device WHERE name=%s', hardware2)
                deviceid = result_id[0].id
            except Exception, ex:
                print ex
        else:
            print '-'

        weeknum = var['weeknum']
        release = var['release'].strip()
        title = var['title'].strip()
        total_cases = var['total_cases']
        total_pass = var['total_pass']
        total_fail = var['total_fail']
        total_na = var['total_na']
        total_measured = var['total_measured']
        created_at = var['created_at'].strip()
        tested_at = var['tested_at'].strip()
        updated_at = var['updated_at'].strip()

        try:
            result = db.query(
                'SELECT count(*) AS total_number FROM crosswalk.reportsummary WHERE qa_id = %s ', int(qa_id))
            if int(result[0].total_number) <= 0:
                db.execute('INSERT INTO reportsummary (qa_id, build_id, profile, branch, darchitecture, testtype, device, hardware, weeknum, srelease, title, total_cases, total_pass, total_fail, total_na, total_measured, created_at, tested_at, updated_at) '
                           'VALUES (%s,%s,%s,%s,%s,%s,%s,%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                           int(qa_id), build_id, profile, branch, architecture, testtype, int(deviceid), hardware, int(weeknum), release, title, int(total_cases), int(total_pass), int(total_fail), int(total_na), int(total_measured), created_at, tested_at, updated_at)
                if enable_rcategory_insert:
                    cfeatures = var['features']
                    for category in cfeatures:
                        qa_id = qa_id
                        cqa_id = category['qa_id']
                        cname = category['name'].strip()
                        ctotal_cases = category['total_cases']
                        ctotal_pass = category['total_pass']
                        ctotal_fail = category['total_fail']
                        ctotal_na = category['total_na']
                        ctotal_measured = category['total_measured']
                        ccomments = category['comments'].strip()
                        try:
                            db.execute('INSERT INTO crosswalk.reportcategory (qa_id, qa_id_category, name, total_cases, total_pass, total_fail, total_na, total_measured, comments) '
                                       'VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                                       int(qa_id), int(cqa_id), cname, int(ctotal_cases), int(ctotal_pass), int(ctotal_fail), int(ctotal_na), int(ctotal_measured), ccomments)
                            if enable_rcase_insert:
                                dcases = category['cases']
                                for dcase in dcases:
                                    qa_id = qa_id
                                    cqa_id = cqa_id
                                    dqa_id = dcase['qa_id']
                                    dname = dcase['name'].strip()
                                    dresult = dcase['result']
                                    dcomment = dcase['comment'].strip()
                                    xbugs = dcase['bugs']
                                    dbugs = ''
                                    for ebug in xbugs:
                                        dbugs = debug, ebug
                                    dbugs = dbugs.strip()
                                    try:
                                        db.execute('INSERT INTO crosswalk.reportcase (qa_id, qa_id_category, qa_id_case, result, name, comment, bugs)'
                                                   'VALUES (%s,%s,%s,%s,%s,%s,%s)',
                                                   int(qa_id), int(cqa_id), int(dqa_id), int(dresult), dname, dcomment, dbugs)
                                    except Exception, ex:
                                        print 'Cases:', qa_id, cqa_id, dqa_id, dname, ex
                        except Exception, ex:
                            print 'Category:', qa_id, cqa_id, ex

                print 'Record inserted: ' + str(qa_id)

            else:
                print 'Record insertion ignored:', str(qa_id), 'existes.'
        except Exception, ex:
            print ex, qa_id

        # DELETE FROM `crosswalk`.`reportcategory` WHERE `id`<'2801';


def renameJSONFile():
    d = datetime.now()
    d = d.strftime('%Y-%m-%d_%H-%M-%S_%f')
    newfile = d + '.json'
    try:
        rename_file(dir, filename, d + '.json')
        print 'json file renamed to ' + newfile + ' successfully'
    except Exception, ex:
        print str(ex) + ': rename json file failed'
    return newfile


def downloadJSONFile():
    try:
        getjson = 'cd ' + dir + '; wget -c --proxy=off "' + url + '"'
        cmd = getjson
        subp = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        c = subp.stdout.readlines()
        print 'json file downloaded successfully'
    except Exception, ex:
        print str(ex) + ': download json file failed'


def main():
    downloadJSONFile()
    jsonToDB(renameJSONFile())
    #jsonToDB('2014-08-15_07-03-30_113457.json')

if __name__ == '__main__':
    main()
