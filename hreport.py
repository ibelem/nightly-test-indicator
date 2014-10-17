# -*- coding: utf-8 -*-
import tornado
# pip install torndb
# apt-get install python-mysqldb
import torndb

from tornado.options import define, options


class ReportHandler(tornado.web.RequestHandler):

    def get(self):
        self.redirect("report/Android/IA/Canary/WebAPI")


class ReportCustomizeHandler(tornado.web.RequestHandler):

    def get(self, profile, architecture, branch, hardware):
        self.db = torndb.Connection(
            host=options.mysql_host, database=options.mysql_database,
            user=options.mysql_user, password=options.mysql_password)

        lprofile = self.db.query(
            'SELECT DISTINCT profile from crosswalk.reportsummary ORDER BY build_id DESC')
        larchitecture = self.db.query(
            'SELECT DISTINCT darchitecture from crosswalk.reportsummary WHERE profile=%s ORDER BY build_id DESC', profile)
        lbranch = self.db.query(
            'SELECT DISTINCT branch from crosswalk.reportsummary WHERE profile=%s AND darchitecture=%s ORDER BY build_id DESC', profile, architecture)
        lhardware = self.db.query(
            'SELECT DISTINCT hardware from crosswalk.reportsummary WHERE profile=%s AND darchitecture=%s AND branch=%s ORDER BY build_id DESC', profile, architecture, branch)

        l = ''

        try:
            if hardware.strip() != '' and hardware.strip() != '0' and hardware != 0:
                l = self.db.query(
                    'SELECT * from crosswalk.reportsummary WHERE profile=%s AND darchitecture=%s AND branch=%s AND hardware=%s order by id DESC LIMIT 12', profile, architecture, branch, hardware)
                if not l:
                    raise tornado.web.HTTPError(404)
                self.render(
                    "report.htm", title="Crosswalk Test Report", l=l, platform=profile, architecture=architecture,
                    branch=branch, hardware=hardware, lprofile=lprofile, larchitecture=larchitecture, lbranch=lbranch, lhardware=lhardware)
            else:
                self.render(
                    "report.htm", title="Crosswalk Test Report", l='', platform=profile, architecture=architecture,
                    branch=branch, hardware=hardware, lprofile=lprofile, larchitecture=larchitecture, lbranch=lbranch, lhardware=lhardware)
        except Exception, ex:
            self.render(
                "report.htm", title="Crosswalk Test Report", l='', platform=profile, architecture=architecture,
                branch=branch, hardware=hardware, lprofile=lprofile, larchitecture=larchitecture, lbranch=lbranch, lhardware=lhardware)
