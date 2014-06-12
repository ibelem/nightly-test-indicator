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
        devices = self.db.query('SELECT * FROM crosswalk.device ORDER BY platform DESC')
        platforms = self.db.query('SELECT DISTINCT platform FROM crosswalk.device')
        architectures = self.db.query('SELECT DISTINCT architecture FROM crosswalk.device')
        priorities = self.db.query('SELECT DISTINCT priority FROM crosswalk.device ORDER BY priority ASC')
        types = self.db.query('SELECT DISTINCT type FROM crosswalk.device')
        sdks = self.db.query('SELECT DISTINCT sdk FROM crosswalk.device')
        results = self.db.query('SELECT * FROM crosswalk.reportsummary where hardware = "nightly" and profile = "android" and architecture = "ia" and branch = "canary" ORDER BY build_id DESC LIMIT 6')
        if not devices: raise tornado.web.HTTPError(404)
        self.render("home.htm", title="Crosswalk Nightly Test Report", results=results, devices=devices, platforms=platforms, architectures=architectures, priorities=priorities, types=types, sdks=sdks)
