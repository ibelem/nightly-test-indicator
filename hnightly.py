# -*- coding: utf-8 -*-
import tornado
# pip install torndb
# apt-get install python-mysqldb
import torndb

from tornado.options import define, options

class NightlyQueryHandler(tornado.web.RequestHandler):
    def post(self):

        self.db = torndb.Connection(
        host=options.mysql_host, database=options.mysql_database,
        user=options.mysql_user, password=options.mysql_password)

        devices = self.db.query('SELECT * FROM crosswalk.device WHERE id IN (SELECT crosswalk.reportsummary.device from crosswalk.reportsummary)')
        if not devices: raise tornado.web.HTTPError(404)
        
        selected = ''
        num = 0
        for device in devices:
            try: 
                deviceid = self.get_argument('id_' + str(device.id))
                num = num + 1
            except Exception, ex:
                print ex            
        if num > 0:
            dvar = globals()
            n = 0
            for device in devices:
                try: 
                    deviceid = self.get_argument('id_' + str(device.id))
                    print str(deviceid)
                    dvar['nr%s' % n] = self.db.query('SELECT DISTINCT * FROM crosswalk.reportsummary AS A INNER JOIN crosswalk.device AS B ON ' + '(A.device=' + str(device.id) + ' AND B.id=' + str(device.id) + ') ORDER BY A.build_id DESC LIMIT 6')
                    if not dvar['nr%s' % n] : raise tornado.web.HTTPError(404)
                    n = n + 1 
                except Exception, ex:
                    print ex  
            l = []
            for i in range(0, num):
                l.append(dvar['nr%s' % i])
            print type(l)
            self.render("nightlyquery.htm", title="Crosswalk Nightly Test Report by Devices", devices=devices, l=l)


        else:
            self.redirect("/")



 
class NightlyHandler(tornado.web.RequestHandler):
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
        if not devices: raise tornado.web.HTTPError(404)
        self.render("nightly.htm", title="Crosswalk Nightly Test - Execution Plan", devices=devices, platforms=platforms, architectures=architectures, priorities=priorities, types=types, sdks=sdks)