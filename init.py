# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web
import tornado.httpclient
import tornado.httpserver
import tornado.options
import os
import hhome, hnightly, hdevice, hreport
# pip install torndb
# apt-get install python-mysqldb
import torndb

from tornado.template import Template

from tornado.options import define, options
define('port', default=8888, help='run the given port', type=int)

define('mysql_host', default='127.0.0.1:3306', help='DB host')
define('mysql_database', default='crosswalk', help='Crosswalk DB')
define('mysql_user', default='root', help='DB User')
define('mysql_password', default='zm179457', help='DB Password')

v_proxy_host = 'proxy.jf.intel.com'
v_proxy_port = 911

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', hhome.HomeHandler),
            (r'/nightly', hnightly.NightlyHandler),
            (r'/device', hdevice.DeviceManagementHandler),
            (r'/device/edit/([0-9]+)', hdevice.DeviceManagementEditHandler),
            (r'/device/add', hdevice.DeviceManagementAddPostHandler),
            (r'/device/update/([0-9]+)', hdevice.DeviceManagementUpdatePostHandler),
            (r'/device/delete/([0-9]+)', hdevice.DeviceManagementDeleteGetHandler),
            (r'/report', hreport.ReportHandler),
            (r'/report/([0-9]+)', hreport.ReportDetailHandler),
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), 'templates'),
            static_path=os.path.join(os.path.dirname(__file__), 'static'),
            debug=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()    

if __name__ == '__main__':
    main()


