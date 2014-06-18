# -*- coding: utf-8 -*-
import tornado
# pip install torndb
# apt-get install python-mysqldb
import torndb

from tornado.options import define, options
  
class ReportHandler(tornado.web.RequestHandler):
    def get(self):
        self.db = torndb.Connection(
        host=options.mysql_host, database=options.mysql_database,
        user=options.mysql_user, password=options.mysql_password)

        avar = globals()
        awvar = globals()
        tvar = globals()
        twvar = globals()
        m= 0
        mw= 0
        n = 0
        nw = 0
        l = []

        avar['mr%s' % m] = self.db.query('SELECT * from crosswalk.reportsummary WHERE profile = "android" AND branch = "canary" AND hardware = "feature" ORDER BY build_id DESC, qa_id DESC LIMIT 16')
        if not avar['mr%s' % m] : raise tornado.web.HTTPError(404)
        m = m + 1 

        awvar['mrw%s' % mw] = self.db.query('SELECT * from crosswalk.reportsummary WHERE profile = "android" AND branch = "canary" AND hardware = "webapi" ORDER BY build_id DESC, qa_id DESC LIMIT 16')
        if not awvar['mrw%s' % mw] : raise tornado.web.HTTPError(404)
        mw = mw + 1 

        tvar['nr%s' % n] = self.db.query('SELECT * from crosswalk.reportsummary WHERE profile = "tizen" AND branch = "canary" AND hardware = "feature" ORDER BY build_id DESC, qa_id DESC LIMIT 16')
        if not tvar['nr%s' % n] : raise tornado.web.HTTPError(404)
        n = n + 1 

        twvar['nrw%s' % nw] = self.db.query('SELECT * from crosswalk.reportsummary WHERE profile = "tizen" AND branch = "canary" AND hardware = "webapi" ORDER BY build_id DESC, qa_id DESC LIMIT 16')
        if not twvar['nrw%s' % nw] : raise tornado.web.HTTPError(404)
        nw = nw + 1 
       
        for i in range(0, m):
            l.append(avar['mr%s' % i])
        for i in range(0, mw):
            l.append(avar['mrw%s' % i])
        for j in range(0, n):
            l.append(tvar['nr%s' % j])
        for j in range(0, nw):
            l.append(tvar['nrw%s' % j])
        self.render("report.htm", title="Crosswalk Nightly Test Report", l=l)
         
class ReportDetailHandler(tornado.web.RequestHandler):
    def get(self, entry_id):
        entries = ['x', 'xx', 'xxx']
        entry = entries[int(entry_id)]
        if not entries: raise tornado.web.HTTPError(404)
        self.render("reportdetail.htm", title="Crosswalk Test Report", entries=entries, entry=entry)
