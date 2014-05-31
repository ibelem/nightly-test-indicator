# -*- coding: utf-8 -*-
import tornado
 
class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        #entries = self.db.query("SELECT * FROM entries ORDER BY date DESC")
        #entry = self.db.get("SELECT * FROM entries WHERE id = %s", entry_id)
        entries = ['x', 'xx', 'xxx']
        if not entries: raise tornado.web.HTTPError(404)
        self.render("view/home.htm", title="Crosswalk Nightly Test", entries=entries)

class ReportHandler(tornado.web.RequestHandler):
     def get(self):
         entries = ['x', 'xx', 'xxx']
         if not entries: raise tornado.web.HTTPError(404)
         self.render("view/report.htm", title="Crosswalk Nightly Test Report", entries=entries)
         
class ReportDetailHandler(tornado.web.RequestHandler):
    def get(self, entry_id):
        entries = ['x', 'xx', 'xxx']
        entry = entries[int(entry_id)]
        if not entries: raise tornado.web.HTTPError(404)
        self.render("view/reportdetail.htm", title="Crosswalk Nightly Test Report", entries=entries, entry=entry)

class FormHandler(tornado.web.RequestHandler):
    def post(self):
        usrname = self.get_argument('usrname')
        psd = self.get_argument('psd')
        self.render("view/form.htm", usr=usrname, pd=psd)
 
 