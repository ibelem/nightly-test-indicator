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
        devices = self.db.query(
            'SELECT * FROM crosswalk.device WHERE id IN (SELECT crosswalk.reportsummary.device from crosswalk.reportsummary WHERE crosswalk.reportsummary.hardware LIKE "Nightly Cordova")')
        if not devices:
            raise tornado.web.HTTPError(404)
        avar = globals()
        m = 0
        l = []

        android = self.db.query(
            'SELECT DISTINCT * FROM crosswalk.device WHERE id IN (SELECT crosswalk.reportsummary.device from crosswalk.reportsummary WHERE (crosswalk.reportsummary.hardware LIKE "nightly cordova") AND platform = "android")')

        build = self.db.query(
            'SELECT DISTINCT build_id FROM crosswalk.reportsummary AS A, crosswalk.device AS B WHERE A.device = B.id AND A.hardware LIKE %s ORDER BY A.qa_id DESC LIMIT 6', '%Cordova')

        for a in android:
            try:
                avar['mr%s' % m] = self.db.query(
                    'SELECT DISTINCT * FROM crosswalk.reportsummary AS A, crosswalk.device AS B WHERE (A.profile=%s AND A.device = B.id) AND B.id=%s AND A.hardware LIKE %s ORDER BY A.qa_id DESC LIMIT 6', a.platform, a.id, '%Cordova')
                print l
                l.append(avar['mr%s' % m])
                m = m + 1
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

        self.render("homecordova.htm", title="Crosswalk based Cordova Nightly Test Report",
                    devices=devices, build=build, l=l)
