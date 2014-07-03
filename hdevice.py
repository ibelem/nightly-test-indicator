# -*- coding: utf-8 -*-
import tornado
# pip install torndb
# apt-get install python-mysqldb
import torndb

from tornado.options import define, options


class DeviceManagementHandler(tornado.web.RequestHandler):

    def get(self):
        self.db = torndb.Connection(
            host=options.mysql_host, database=options.mysql_database,
            user=options.mysql_user, password=options.mysql_password)
        results = self.db.query(
            "SELECT * FROM crosswalk.device ORDER BY platform ASC")
        #if not entries: raise tornado.web.HTTPError(404)
        self.render(
            "device.htm", title="Crosswalk Nightly Test Device Management", results=results)


class DeviceManagementEditHandler(tornado.web.RequestHandler):

    def get(self, entry_id):
        self.db = torndb.Connection(
            host=options.mysql_host, database=options.mysql_database,
            user=options.mysql_user, password=options.mysql_password)
        results = self.db.query(
            "SELECT * FROM crosswalk.device ORDER BY platform ASC")
        entry_id = int(entry_id)
        #if not entries: raise tornado.web.HTTPError(404)
        self.render(
            "deviceupdate.htm", title="Crosswalk Nightly Test Device Management - Edit",
            results=results, entry_id=entry_id)


class DeviceManagementAddPostHandler(tornado.web.RequestHandler):

    def post(self):
        devicename = self.get_argument('devicename')
        try:
            type = self.get_argument('type')
        except Exception, ex:
            type = ''
        try:
            asset = self.get_argument('asset')
        except Exception, ex:
            asset = ''
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
        self.db.execute("INSERT INTO device (name, type, asset, priority, platform, architecture, sdk, serial, note, date) "
                        "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,'', now())",
                        devicename, type, asset, priority, platform, architecture, sdk, serial)
        self.redirect("/device")


class DeviceManagementUpdatePostHandler(tornado.web.RequestHandler):

    def post(self, entry_id):
        try:
            devicename = self.get_argument('uname')
        except Exception, ex:
            devicename = ''
        try:
            type = self.get_argument('utype')
        except Exception, ex:
            type = ''
        try:
            asset = self.get_argument('uasset')
        except Exception, ex:
            asset = ''
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
        self.db.execute(
            "UPDATE crosswalk.device SET name=%s, type=%s, asset=%s, priority=%s, platform=%s, architecture=%s, sdk=%s, serial=%s, date=now() WHERE id=%s",
            devicename, type, asset, priority, platform, architecture, sdk, serial, int(entry_id))
        self.redirect("/device")


class DeviceManagementDeleteGetHandler(tornado.web.RequestHandler):

    def get(self, entry_id):
        self.db = torndb.Connection(
            host=options.mysql_host, database=options.mysql_database,
            user=options.mysql_user, password=options.mysql_password)
        self.db.execute(
            "DELETE FROM crosswalk.device WHERE id=%s", int(entry_id))
        self.redirect("/device")
