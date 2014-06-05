# -*- coding: utf-8 -*-
import tornado
# pip install torndb
# apt-get install python-mysqldb
import torndb
import json 

from tornado.options import define, options
 
class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        #entries = self.db.query("SELECT * FROM entries ORDER BY date DESC")
        #entry = self.db.get("SELECT * FROM entries WHERE id = %s", entry_id)
        #entries = ['x', 'xx', 'xxx']
        #if not entries: raise tornado.web.HTTPError(404)
        #self.render("view/home.htm", title="Crosswalk Nightly Test", entries=entries)
        self.db = torndb.Connection(
                host=options.mysql_host, database=options.mysql_database,
                user=options.mysql_user, password=options.mysql_password)
        devices = self.db.query("SELECT name FROM crosswalk.device")
	#self.write(devices)
	if not devices: raise tornado.web.HTTPError(404)
        self.render("view/home.htm", title="Crosswalk Nightly Test", devices=devices)

class DeviceManagementHandler(tornado.web.RequestHandler):
    def get(self):
        self.db = torndb.Connection(
        host=options.mysql_host, database=options.mysql_database,
        user=options.mysql_user, password=options.mysql_password)
        results = self.db.query("SELECT * FROM crosswalk.device order by platform")
        #if not entries: raise tornado.web.HTTPError(404)
        self.render("view/device.htm", title="Crosswalk Nightly Test Device Management", results=results)

class DeviceManagementAddPostHandler(tornado.web.RequestHandler):
    def post(self):
        platform = self.get_argument('platform')
        if platform == 'android':
            platform = 0
        else:
            platform = 1 
        architecture = self.get_argument('architecture')
        if architecture == 'ia':
            architecture = 0
        else:
            architecture = 1
        devicename = self.get_argument('devicename')
        try:
            sdk = self.get_argument('sdk')
        except Exception, ex:
            sdk = ''
        try:
            serial = self.get_argument('serial')
        except Exception, ex:
            serial = ''
        self.db = torndb.Connection(
                host=options.mysql_host, database=options.mysql_database,
                user=options.mysql_user, password=options.mysql_password)
        self.db.execute("INSERT INTO device (name, platform, architecture, sdk, serial, note, date) "
            "VALUES (%s,%s,%s,%s,%s,'', UTC_TIMESTAMP())", 
            devicename, platform, architecture, sdk, serial)
        self.redirect("/device")
        
class DeviceManagementDeleteGetHandler(tornado.web.RequestHandler):
    def get(self, entry_id):
        self.db = torndb.Connection(
        host=options.mysql_host, database=options.mysql_database,
        user=options.mysql_user, password=options.mysql_password)
        self.db.execute("delete from crosswalk.device where id=%s", entry_id)
        self.redirect("/device")

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
