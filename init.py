# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web
import tornado.httpclient
import tornado.options
import os
import uimodules
# pip install torndb
# apt-get install python-mysqldb
import torndb

from tornado.template import Template

from tornado.options import define, options
define('port', default=8888, help='run the given port', type=int)

define("mysql_host", default="127.0.0.1:3306", help="database host")
define("mysql_database", default="crosswalk", help="Crosswalk Database")
define("mysql_user", default="root", help="DB User")
define("mysql_password", default="zm179457", help="DB Password")

v_proxy_host = 'proxy.jf.intel.com'
v_proxy_port = 911

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application([
        (r'/', uimodules.HomeHandler),
        (r'/device', uimodules.DeviceManagementHandler),
        (r'/device/edit/([0-9]+)', uimodules.DeviceManagementEditHandler),
        (r'/device/add/p', uimodules.DeviceManagementAddPostHandler),
        (r'/device/update/([0-9]+)', uimodules.DeviceManagementUpdatePostHandler),
        (r'/device/delete/([0-9]+)', uimodules.DeviceManagementDeleteGetHandler),
        (r'/report', uimodules.ReportHandler),
        (r'/report/([0-9]+)', uimodules.ReportDetailHandler),
        #template_path = os.path.join(os.path.dirname(__file__), 'templates')
    ])
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


