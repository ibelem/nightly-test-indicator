# -*- coding: utf-8 -*-
import tornado
# pip install torndb
# apt-get install python-mysqldb
import torndb

from tornado.options import define, options
 
class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        self.db = torndb.Connection(
        host=options.mysql_host, database=options.mysql_database,
        user=options.mysql_user, password=options.mysql_password)
        devices = self.db.query('SELECT * FROM crosswalk.device WHERE id IN (SELECT crosswalk.reportsummary.device from crosswalk.reportsummary)')
        if not devices: raise tornado.web.HTTPError(404)
        avar = globals()
        tvar = globals()
        m= 0
        n = 0
        l = []
        t = []
        
        android = self.db.query('SELECT DISTINCT * FROM crosswalk.device WHERE id IN (SELECT crosswalk.reportsummary.device from crosswalk.reportsummary) and platform = \'android\'')
        tizen = self.db.query('SELECT DISTINCT * FROM crosswalk.device WHERE id IN (SELECT crosswalk.reportsummary.device from crosswalk.reportsummary) and platform = \'tizen\'')

        for a in android:
            try:    
                avar['mr%s' % m] = self.db.query('SELECT DISTINCT * FROM crosswalk.reportsummary AS A, crosswalk.device AS B WHERE (A.profile=%s AND A.device = B.id) AND B.id=%s ORDER BY A.build_id DESC, A.qa_id DESC LIMIT 6', a.platform, a.id);
                l.append(avar['mr%s' % m])
                m = m + 1 
            except Exception, ex:
                print ex           

        for b in tizen:
            try:    
                avar['nr%s' % n] = self.db.query('SELECT DISTINCT * FROM crosswalk.reportsummary AS A, crosswalk.device AS B WHERE (A.profile=%s AND A.device = B.id) AND B.id=%s ORDER BY A.build_id DESC, A.qa_id DESC LIMIT 6', b.platform, b.id);
                t.append(avar['nr%s' % n])
                n = n + 1 
            except Exception, ex:
                print ex 

#        for d in devices:
#            try: 
#                if d.platform.lower() == 'android':
#                    avar['mr%s' % m] = self.db.query('SELECT DISTINCT * FROM crosswalk.reportsummary AS A, crosswalk.device AS B WHERE (A.profile=%s AND A.device = B.id) ORDER BY A.build_id DESC, A.qa_id DESC LIMIT 6', d.platform)
#                    if not avar['mr%s' % m] : raise tornado.web.HTTPError(404)
#                    m = m + 1 
#                else:
#                    tvar['nr%s' % n] = self.db.query('SELECT DISTINCT * FROM crosswalk.reportsummary AS A, crosswalk.device AS B WHERE (A.profile=%s AND A.device = B.id) ORDER BY A.build_id DESC, A.qa_id DESC LIMIT 6', d.platform)
#                    if not tvar['nr%s' % n] : raise tornado.web.HTTPError(404)
#                    n = n + 1 
#            except Exception, ex:
#                print ex          
#        for i in range(0, m):
#            l.append(avar['mr%s' % i])
#        for j in range(0, n):
#            t.append(tvar['nr%s' % j])

        self.render("home.htm", title="Crosswalk Nightly Test Report", devices=devices, l=l, t=t)

