# -*- coding: utf-8 -*-
import tornado
# pip install torndb
# apt-get install python-mysqldb
import torndb

from tornado.options import define, options


class NightlyQueryGetHandler(tornado.web.RequestHandler):

    def get(self, entry_id):
        self.db = torndb.Connection(
            host=options.mysql_host, database=options.mysql_database,
            user=options.mysql_user, password=options.mysql_password)
        devices = self.db.query(
            'SELECT * FROM crosswalk.device WHERE id IN (SELECT crosswalk.reportsummary.device from crosswalk.reportsummary)')
        if not devices:
            self.render("nightlyquerygetno.htm",
                        title="Crosswalk Nightly Test Report by Devices", devices=devices, d=entry_id)
        device = self.db.query(
            'SELECT * FROM crosswalk.device WHERE id = %s', entry_id)
        if not device:
            self.render("nightlyquerygetno.htm",
                        title="Crosswalk Nightly Test Report by Devices", devices=devices, d=entry_id)
        l = self.db.query('SELECT DISTINCT * FROM crosswalk.reportsummary AS A INNER JOIN crosswalk.device AS B ON ' +
                          '(A.device=' + str(entry_id) + ' AND B.id=' + str(entry_id) + ') ORDER BY A.build_id DESC, A.qa_id DESC LIMIT 16')
        if not l:
            self.render("nightlyquerygetno.htm",
                        title="Crosswalk Nightly Test Report by Devices", devices=devices, d=entry_id)
        self.render(
            "nightlyqueryget.htm", title="Crosswalk Nightly Test Report by Devices",
            devices=devices, d=entry_id, list=l)


class NightlyQueryHandler(tornado.web.RequestHandler):

    def post(self):

        self.db = torndb.Connection(
            host=options.mysql_host, database=options.mysql_database,
            user=options.mysql_user, password=options.mysql_password)

        devices = self.db.query(
            'SELECT * FROM crosswalk.device WHERE id IN (SELECT crosswalk.reportsummary.device from crosswalk.reportsummary)')
        if not devices:
            raise tornado.web.HTTPError(404)

        selected = ''
        num = 0
        cate = []
        for device in devices:
            try:
                deviceid = self.get_argument('id_' + str(device.id))
                num = num + 1
            except Exception, ex:
                print ex
        if num > 0:
            dvar = globals()
            lvar = globals()
            n = 0
            for device in devices:
                try:
                    deviceid = self.get_argument('id_' + str(device.id))
                    print str(deviceid)
                    dvar['di%s' % n] = str(device.id)
                    lvar['nr%s' % n] = self.db.query('SELECT DISTINCT * FROM crosswalk.reportsummary AS A INNER JOIN crosswalk.device AS B ON ' +
                                                     '(A.device=' + str(device.id) + ' AND B.id=' + str(device.id) + ') ORDER BY A.build_id DESC, A.qa_id DESC LIMIT 16')

                    # SELECT DISTINCT * FROM crosswalk.reportsummary AS A INNER JOIN crosswalk.device AS B ON (A.device='24' AND B.id='24') ORDER BY A.build_id DESC, A.qa_id DESC LIMIT 2
                    
                    if num == 1:
                        qa_id = self.db.query('SELECT DISTINCT * FROM crosswalk.reportsummary AS A INNER JOIN crosswalk.device AS B ON ' + 
                                                    '(A.device=' + str(device.id) + ' AND B.id=' + str(device.id) + ') ORDER BY A.build_id DESC, A.qa_id DESC LIMIT 2')
                        if not qa_id:
                            cate= []
                        for qid in qa_id:
                            try:
                                cateresults = self.db.query('SELECT DISTINCT qa_id, qa_id_category, total_cases, name, total_pass, total_fail, total_na, total_measured, comments, note FROM crosswalk.reportcategory where qa_id = %s ORDER BY name ASC', qid.qa_id)
                                cate.append(cateresults)
                            except Exception, ex:
                                print ex

                    if not lvar['nr%s' % n]:
                        raise tornado.web.HTTPError(404)
                    n = n + 1
                except Exception, ex:
                    print ex
            d = []
            for j in range(0, num):
                d.append(dvar['di%s' % j])
            l = []
            for i in range(0, num):
                l.append(lvar['nr%s' % i])
            self.render(
                "nightlyquery.htm", title="Crosswalk Nightly Test Report by Devices", devices=devices, d=d, l=l, cate=cate, num=num)
        else:
            self.redirect("/")


class NightlyHandler(tornado.web.RequestHandler):

    def get(self):
        self.db = torndb.Connection(
            host=options.mysql_host, database=options.mysql_database,
            user=options.mysql_user, password=options.mysql_password)
        devices = self.db.query(
            'SELECT * FROM crosswalk.device ORDER BY platform DESC')
        platforms = self.db.query(
            'SELECT DISTINCT platform FROM crosswalk.device')
        architectures = self.db.query(
            'SELECT DISTINCT architecture FROM crosswalk.device')
        priorities = self.db.query(
            'SELECT DISTINCT priority FROM crosswalk.device ORDER BY priority ASC')
        types = self.db.query('SELECT DISTINCT type FROM crosswalk.device')
        sdks = self.db.query('SELECT DISTINCT sdk FROM crosswalk.device')
        if not devices:
            raise tornado.web.HTTPError(404)
        self.render(
            "nightly.htm", title="Crosswalk Nightly Test - Execution Plan", devices=devices,
            platforms=platforms, architectures=architectures, priorities=priorities, types=types, sdks=sdks)
