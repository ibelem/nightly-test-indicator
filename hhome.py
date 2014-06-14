# -*- coding: utf-8 -*-
import tornado
# pip install torndb
# apt-get install python-mysqldb
import torndb

from tornado.options import define, options
 
class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        self.db = torndb.Connection(
        host=options.mysql_host, database=options.mysql_database,
        user=options.mysql_user, password=options.mysql_password)
 
        results = self.db.query('SELECT * FROM crosswalk.reportsummary where hardware = "nightly" and profile = "android" and architecture = "ia" and branch = "canary" ORDER BY build_id DESC LIMIT 6')
        results_asus_t00e = self.db.query('SELECT * FROM crosswalk.reportsummary where hardware = "temp" and profile = "android" and architecture = "ia" and branch = "canary" ORDER BY build_id DESC LIMIT 6')
        results_tc_acer = self.db.query('SELECT * FROM crosswalk.reportsummary WHERE hardware ="nightly" AND profile = "tizen" AND branch = "canary" ORDER BY build_id DESC LIMIT 6')
        
        devices = self.db.query('SELECT * FROM crosswalk.device WHERE id IN (SELECT crosswalk.reportsummary.device from crosswalk.reportsummary)')
        if not devices: raise tornado.web.HTTPError(404)
        self.render("home.htm", title="Crosswalk Nightly Test Report", results=results, results_asus_t00e=results_asus_t00e, results_tc_acer=results_tc_acer, devices=devices)

