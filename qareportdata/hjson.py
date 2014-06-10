# -*- coding: utf-8 -*-

import urllib2,urllib  
import simplejson as json

url = ('http://wrt-qa-report.sh.intel.com/api/reports/?auth_token=NL1sbHvpDadoM4jrml7A&limit_amount=5&id=2815') 
  
request = urllib2.Request( 
    url, None, {'Referer': 'http://wrt-qa-report.sh.intel.com'}) 
response = urllib2.urlopen(request) 

results = json.load(response) 
 