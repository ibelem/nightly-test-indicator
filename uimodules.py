# -*- coding: utf-8 -*-
import tornado
 
class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        #entries = self.db.query("SELECT * FROM entries ORDER BY date DESC")
        #entry = self.db.get("SELECT * FROM entries WHERE id = %s", entry_id)
        entries = ['i7', 'xeon', '中国汉字']
        if not entries: raise tornado.web.HTTPError(404)
        self.render("view/home.htm", title="Crosswalk Nightly Test", entries=entries)
 
class ReportHandler(tornado.web.RequestHandler):
    def get(self, entry_id):
        entries = ['i7', 'xeon', '中国汉字']
        entry = entries[int(entry_id)]
        if not entries: raise tornado.web.HTTPError(404)
        self.render("view/report.htm", title="Crosswalk Nightly Test Report", entries=entries, entry=entry)


 
 