# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web
import tornado.httpclient
import tornado.httpserver
import tornado.options
import os
import hhome, hnightly, hdevice, hreport, hhomecordova, hnightlycordova
# pip install torndb
# apt-get install python-mysqldb
import torndb

from tornado.template import Template

from tornado.options import define, options
define('port', default=8080, help='run the given port', type=int)

define('mysql_host', default='127.0.0.1:3306', help='DB host')
define('mysql_database', default='crosswalk', help='Crosswalk DB')
define('mysql_user', default='root', help='DB User')
define('mysql_password', default='', help='DB Password')

v_proxy_host = ''
v_proxy_port = 911

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', hhome.HomeHandler),
            (r'/nightly/query', hnightly.NightlyQueryHandler),
            (r'/nightly/([0-9]+)', hnightly.NightlyQueryGetHandler),
            (r'/nightly', hnightly.NightlyHandler),
            (r'/cordova', hhomecordova.HomeHandler),
            (r'/nightlycordova/querycordova', hnightlycordova.NightlyQueryHandler),
            (r'/nightlycordova/([0-9]+)', hnightlycordova.NightlyQueryGetHandler),
            (r'/device', hdevice.DeviceManagementHandler),
            (r'/device/edit/([0-9]+)', hdevice.DeviceManagementEditHandler),
            (r'/device/add', hdevice.DeviceManagementAddPostHandler),
            (r'/device/update/([0-9]+)', hdevice.DeviceManagementUpdatePostHandler),
            (r'/device/delete/([0-9]+)', hdevice.DeviceManagementDeleteGetHandler),
            (r'/report', hreport.ReportHandler),
            (r'/report/(\w+)/(\w+)/(\w+)/([\w(%20)*]+)', hreport.ReportCustomizeHandler),

#            (r'/report/(\w+)', hreport.ReportPlatformHandler),
#            (r'/report/Android', hreport.ReportPlatformArchitectureAHandler),
#            (r'/report/Android/IA', hreport.ReportPlatformArchitectureAIAHandler),
#            (r'/report/Android/ARM', hreport.ReportPlatformArchitectureAARMHandler),
#            (r'/report/Tizen/(\w+)', hreport.ReportPlatformArchitectureTHandler),
#            (r'/report/Tizen/Generic/(\w+)', hreport.ReportPlatformArchitectureTGenericHandler),
#            (r'/report/Tizen/Common/(\w+)', hreport.ReportPlatformArchitectureTCommonHandler),
#            (r'/report/Tizen/IVI/(\w+)', hreport.ReportPlatformArchitectureTIVIHandler),

        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), 'templates'),
            static_path=os.path.join(os.path.dirname(__file__), 'static'),
            debug=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)

def main():
    tornado.options.parse_config_file("config.conf")
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application(), xheaders=True)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()    

if __name__ == '__main__':
    main()


