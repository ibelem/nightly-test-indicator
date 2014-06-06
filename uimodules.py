# -*- coding: utf-8 -*-
import tornado
# pip install torndb
# apt-get install python-mysqldb
import torndb
import json 

from tornado.options import define, options
 
class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        self.db = torndb.Connection(
                host=options.mysql_host, database=options.mysql_database,
                user=options.mysql_user, password=options.mysql_password)
        devices = self.db.query("SELECT name FROM crosswalk.device")
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

class DeviceManagementEditHandler(tornado.web.RequestHandler):
    def get(self, entry_id):
        self.db = torndb.Connection(
        host=options.mysql_host, database=options.mysql_database,
        user=options.mysql_user, password=options.mysql_password)
        results = self.db.query("SELECT * FROM crosswalk.device order by platform")
        entry_id = int(entry_id)
        #if not entries: raise tornado.web.HTTPError(404)
        self.render("view/deviceupdate.htm", title="Crosswalk Nightly Test Device Management", results=results, entry_id=entry_id)

class DeviceManagementAddPostHandler(tornado.web.RequestHandler):
    def post(self):
        devicename = self.get_argument('devicename')
        try:
            priority = self.get_argument('priority')
        except Exception, ex:
            priority = ''
        try:
            platform = self.get_argument('platform')
        except Exception, ex:
            platform = ''
        try:
            architecture = self.get_argument('architecture')
        except Exception, ex:
            architecture = ''    
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
        self.db.execute("INSERT INTO device (name, priority, platform, architecture, sdk, serial, note, date) "
            "VALUES (%s,%s,%s,%s,%s,%s,'', now())", 
            devicename, priority, platform, architecture, sdk, serial)
        self.redirect("/device")

class DeviceManagementUpdatePostHandler(tornado.web.RequestHandler):
    def post(self, entry_id):
        try:
            devicename = self.get_argument('uname')
        except Exception, ex:
            devicename = ''
        try:
            priority = self.get_argument('upriority')
        except Exception, ex:
            priority = ''
        try:
            platform = self.get_argument('uplatform')
        except Exception, ex:
            platform = ''
        try:
            architecture = self.get_argument('uarchitecture')
        except Exception, ex:
            architecture = ''    
        try:
            sdk = self.get_argument('usdk')
        except Exception, ex:
            sdk = ''
        try:
            serial = self.get_argument('userial')
        except Exception, ex:
            serial = ''
        self.db = torndb.Connection(
                host=options.mysql_host, database=options.mysql_database,
                user=options.mysql_user, password=options.mysql_password)
        self.db.execute("UPDATE crosswalk.device SET name=%s, priority=%s, platform=%s, architecture=%s, sdk=%s, serial=%s, date=now() WHERE id=%s", 
            devicename, priority, platform, architecture, sdk, serial, int(entry_id))
        self.redirect("/device")
        
class DeviceManagementDeleteGetHandler(tornado.web.RequestHandler):
    def get(self, entry_id):
        self.db = torndb.Connection(
        host=options.mysql_host, database=options.mysql_database,
        user=options.mysql_user, password=options.mysql_password)
        self.db.execute("DELETE FROM crosswalk.device WHERE id=%s", int(entry_id))
        self.redirect("/device")

class ReportHandler(tornado.web.RequestHandler):
     def get(self):
         entries = ['x', 'xx', 'xxx']
         if not entries: raise tornado.web.HTTPError(404)
         self.render("view/report.htm", title="Crosswalk Test Report", entries=entries)
         
class ReportDetailHandler(tornado.web.RequestHandler):
    def get(self, entry_id):
        entries = ['x', 'xx', 'xxx']
        entry = entries[int(entry_id)]
        if not entries: raise tornado.web.HTTPError(404)
        self.render("view/reportdetail.htm", title="Crosswalk Nightly Test Report", entries=entries, entry=entry)
