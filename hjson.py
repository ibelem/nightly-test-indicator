# -*- coding: utf-8 -*-

import urllib2,urllib  
#import simplejson
from tornado.options import define, options
import json
import socks
import socket


define('mysql_host', default='127.0.0.1:3306', help='database host')
define('mysql_database', default='crosswalk', help='Crosswalk Database')
define('mysql_user', default='root', help='DB User')
define('mysql_password', default='zm179457', help='DB Password')

define('protocol', default='http')
define('host', default='wrt-qa-report.sh.intel.com')
define('path', default='api/reports')
define('auto_token', 'NL1sbHvpDadoM4jrml7A')
define('id','2815')
define('limit_amount','1')

v_proxy_host = 'proxy.jf.intel.com'
v_proxy_port = 1080
#v_proxy_type = 'http'

def main():
    config = [options.protocol,options.host,options.path,options.auto_token, options.id, options.limit_amount]
    url = '%s://%s/%s/?auto_token=%s&id=%s&limit_amount=%s' % tuple(config)
    #url = 'http://cnaqi.com/api/j/?cid=1&shortdate=1&v=0'
    print url
    result = ''

    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, v_proxy_host, v_proxy_port)
    socket.socket = socks.socksocket
    try:
        request = urllib2.Request(url, None, {'Referer': url}) 
        #request.set_proxy(v_proxy_host + ':' + str(v_proxy_port), v_proxy_type)
        response = urllib2.urlopen(request) 
        result = json.load(response) 
    except Exception, ex:
        result = ex;
    print result 

if __name__ == '__main__':
    main()

 