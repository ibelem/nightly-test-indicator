# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web
import tornado.httpclient
import tornado.options
import uimodules

from tornado.options import define, options
define('port', default=8888, help='run the give port', type=int)

v_proxy_host = 'proxy.jf.intel.com'
v_proxy_port = 911

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application([
        (r"/", uimodules.HomeHandler),
        (r"/report/([0-9]+)", uimodules.ReportHandler),
        (r"/ansc", AsycHandler),
    ])
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
