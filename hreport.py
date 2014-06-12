# -*- coding: utf-8 -*-
import tornado
# pip install torndb
# apt-get install python-mysqldb
import torndb

from tornado.options import define, options
  
class ReportHandler(tornado.web.RequestHandler):
     def get(self):
         entries = ['x', 'xx', 'xxx']
         if not entries: raise tornado.web.HTTPError(404)
         self.render("report.htm", title="Crosswalk Test Report", entries=entries)
         
class ReportDetailHandler(tornado.web.RequestHandler):
    def get(self, entry_id):
        entries = ['x', 'xx', 'xxx']
        entry = entries[int(entry_id)]
        if not entries: raise tornado.web.HTTPError(404)
        self.render("reportdetail.htm", title="Crosswalk Test Report", entries=entries, entry=entry)
