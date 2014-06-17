# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import re
import subprocess
from subprocess import call
from datetime import *  
import time  
import simplejson
import tornado
import torndb

mysql_host = '127.0.0.1'
mysql_port = 3306
mysql_database = 'crosswalk'
mysql_user = 'root'
mysql_password = 'zm179457'

protocol = 'http'
host = 'wrt-qa-report.sh.intel.com'
path = 'api/reports'
auto_token = 'NL1sbHvpDadoM4jrml7A'
limit_amount = '6'
config = [protocol, host, path, auto_token, limit_amount]
url = '%s://%s/%s/?auto_token=%s&limit_amount=%s' % tuple(config)
filename = 'index.html?auto_token='+ auto_token + '&limit_amount=' + limit_amount
dir = '/home/belem/webqa-dev/nightly_indicator/qareportdata/data'

def jsonToDB(file):
    fp = open(dir + '/' + file)
    reader = fp.read()
    d = simplejson.loads(reader, strict=False)
    for var in d:
        qa_id = var['qa_id']
        build_id = var['build_id'].strip()
        profile = var['profile'].strip()
        testtype = var['testtype'].strip()
        ab = testtype.lower()
        branch = ''
        architecture = ''
        if ab.endswith('canary'):
            branch = 'Canary'
            architecture = testtype.replace('Canary', '').replace('canary', '').replace('Tizen', '').replace('tizen', '').strip()
        elif ab.endswith('beta'):
            branch = 'Beta'
            architecture = testtype.replace('Beta', '').replace('beta', '').replace('Tizen', '').replace('tizen', '').strip()
        elif ab.endswith('stable'):
            branch = 'Stable'
            architecture = testtype.replace('Stable', '').replace('stable', '').replace('Tizen', '').replace('tizen', '').strip()
        else:
            branch = ''
            architecture = testtype.strip()
        
        hardware = var['hardware'].strip()
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

        db = torndb.Connection(
                host=mysql_host, database=mysql_database,
                user=mysql_user, password=mysql_password)
     
        try:
            result = db.query('SELECT count(*) AS total_number FROM crosswalk.reportsummary WHERE qa_id = %s ', int(qa_id))
            if int(result[0].total_number) <= 0:
                db.execute('INSERT INTO reportsummary (qa_id, build_id, profile, branch, darchitecture, testtype, hardware, weeknum, srelease, title, total_cases, total_pass, total_fail, total_na, total_measured, created_at, tested_at, updated_at) '
                    'VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', 
                    int(qa_id), build_id, profile, branch, architecture, testtype, hardware, int(weeknum), release, title, int(total_cases), int(total_pass), int(total_fail), int(total_na), int(total_measured), created_at, tested_at, updated_at)
                
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
               print 'Record insertion ignored:',str(qa_id),'existes.' 
        except Exception, ex: 
            print ex, qa_id

        #DELETE FROM `crosswalk`.`reportcategory` WHERE `id`<'2801';
        
def renameJSONFile():
    d = datetime.now()
    d = d.strftime('%Y-%m-%d_%H-%M-%S_%f')
    newfile = d + '.json'
    try:
        renameFile(dir, filename, d + '.json')
        print 'json file renamed to '+ newfile +' successfully'
    except Exception, ex:
        print str(ex) + ': rename json file failed'    
    return newfile

def renameFile(dir, na, nb):
    files = os.listdir(dir)
    for i in files:
        if i.find(na) > -1:
            f_path = dir + os.sep + i
            if os.path.isfile(f_path):
                os.rename(f_path, dir + os.sep + i.replace(na,nb))
 
def downloadJSONFile():
  try:
    getjson = 'cd data; wget -c --proxy=off "'+ url +'"'
    cmd = getjson
    subp=subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    c=subp.stdout.readlines()
    print 'json file downloaded successfully'
  except Exception, ex:
    print str(ex) + ': download json file failed' 

def main():
  downloadJSONFile()
  jsonToDB(renameJSONFile())
  #jsonToDB('2014-06-12_11-32-06_162615.json')

if __name__ == '__main__':
  main()
