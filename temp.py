# -*- coding: utf-8 -*-
import tornado
# pip install torndb
# apt-get install python-mysqldb
import torndb

from tornado.options import define, options
  
class ReportHandler(tornado.web.RequestHandler):
    def get(self):
        self.db = torndb.Connection(
        host=options.mysql_host, database=options.mysql_database,
        user=options.mysql_user, password=options.mysql_password)

        lprofile = self.db.query('SELECT DISTINCT profile from crosswalk.reportsummary ORDER BY build_id DESC')
        larchitecture = self.db.query('SELECT DISTINCT darchitecture from crosswalk.reportsummary ORDER BY build_id DESC')
        lbranch = self.db.query('SELECT DISTINCT branch from crosswalk.reportsummary ORDER BY build_id DESC')
        lhardware = self.db.query('SELECT DISTINCT hardware from crosswalk.reportsummary ORDER BY build_id DESC')

        platform = ''
        architecture = ''
        branch = ''
        hardware = ''

        avar = globals()
        awvar = globals()
        tvar = globals()
        twvar = globals()
        m= 0
        mw= 0
        n = 0
        nw = 0
        l = []
        avar['mr%s' % m] = self.db.query('SELECT * from crosswalk.reportsummary WHERE profile = "android" AND branch = "canary" AND hardware = "feature" ORDER BY build_id DESC, qa_id DESC LIMIT 16')
        if not avar['mr%s' % m] : raise tornado.web.HTTPError(404)
        m = m + 1 
        awvar['mrw%s' % mw] = self.db.query('SELECT * from crosswalk.reportsummary WHERE profile = "android" AND branch = "canary" AND hardware = "webapi" ORDER BY build_id DESC, qa_id DESC LIMIT 16')
        if not awvar['mrw%s' % mw] : raise tornado.web.HTTPError(404)
        mw = mw + 1 
        tvar['nr%s' % n] = self.db.query('SELECT * from crosswalk.reportsummary WHERE profile = "tizen" AND branch = "canary" AND hardware = "feature" ORDER BY build_id DESC, qa_id DESC LIMIT 16')
        if not tvar['nr%s' % n] : raise tornado.web.HTTPError(404)
        n = n + 1 
        twvar['nrw%s' % nw] = self.db.query('SELECT * from crosswalk.reportsummary WHERE profile = "tizen" AND branch = "canary" AND hardware = "webapi" ORDER BY build_id DESC, qa_id DESC LIMIT 16')
        if not twvar['nrw%s' % nw] : raise tornado.web.HTTPError(404)
        nw = nw + 1 
       
        for i in range(0, m):
            l.append(avar['mr%s' % i])
        for i in range(0, mw):
            l.append(avar['mrw%s' % i])
        for j in range(0, n):
            l.append(tvar['nr%s' % j])
        for j in range(0, nw):
            l.append(tvar['nrw%s' % j])
        self.render("report.htm", title="Crosswalk Nightly Test Report", l=l, platform=platform, architecture=architecture, branch=branch, hardware=hardware, lprofile=lprofile, larchitecture=larchitecture, lbranch=lbranch, lhardware=lhardware)

class ReportPlatformHandler(tornado.web.RequestHandler):
    def get(self, platform):
        self.db = torndb.Connection(
        host=options.mysql_host, database=options.mysql_database,
        user=options.mysql_user, password=options.mysql_password)

        platform = platform
        platformlow = platform.lower()
        architecture = ''
        branch = ''
        hardware = ''

        lprofile = self.db.query('SELECT DISTINCT profile from crosswalk.reportsummary ORDER BY build_id DESC')
        larchitecture = self.db.query('SELECT DISTINCT darchitecture from crosswalk.reportsummary WHERE profile=%s ORDER BY build_id DESC', platformlow)
        lbranch = self.db.query('SELECT DISTINCT branch from crosswalk.reportsummary WHERE profile=%s ORDER BY build_id DESC', platformlow)
        lhardware = self.db.query('SELECT DISTINCT hardware from crosswalk.reportsummary WHERE profile=%s ORDER BY build_id DESC', platformlow)

        avar = globals()
        awvar = globals()
        tvar = globals()
        twvar = globals()
        m= 0
        mw= 0
        n = 0
        nw = 0
        l = []
        avar['mr%s' % m] = self.db.query('SELECT * from crosswalk.reportsummary WHERE profile = "android" AND branch = "canary" AND hardware = "feature" ORDER BY build_id DESC, qa_id DESC LIMIT 16')
        if not avar['mr%s' % m] : raise tornado.web.HTTPError(404)
        m = m + 1 
        awvar['mrw%s' % mw] = self.db.query('SELECT * from crosswalk.reportsummary WHERE profile = "android" AND branch = "canary" AND hardware = "webapi" ORDER BY build_id DESC, qa_id DESC LIMIT 16')
        if not awvar['mrw%s' % mw] : raise tornado.web.HTTPError(404)
        mw = mw + 1 
        tvar['nr%s' % n] = self.db.query('SELECT * from crosswalk.reportsummary WHERE profile = "tizen" AND branch = "canary" AND hardware = "feature" ORDER BY build_id DESC, qa_id DESC LIMIT 16')
        if not tvar['nr%s' % n] : raise tornado.web.HTTPError(404)
        n = n + 1 
        twvar['nrw%s' % nw] = self.db.query('SELECT * from crosswalk.reportsummary WHERE profile = "tizen" AND branch = "canary" AND hardware = "webapi" ORDER BY build_id DESC, qa_id DESC LIMIT 16')
        if not twvar['nrw%s' % nw] : raise tornado.web.HTTPError(404)
        nw = nw + 1 
       
        for i in range(0, m):
            l.append(avar['mr%s' % i])
        for i in range(0, mw):
            l.append(avar['mrw%s' % i])
        for j in range(0, n):
            l.append(tvar['nr%s' % j])
        for j in range(0, nw):
            l.append(tvar['nrw%s' % j])
        self.render("report.htm", title="Crosswalk Nightly Test Report", l=l, platform = platform, architecture=architecture, branch=branch, hardware=hardware, lprofile=lprofile, larchitecture=larchitecture, lbranch=lbranch, lhardware=lhardware)

class ReportPlatformArchitectureAHandler(tornado.web.RequestHandler):
    def get(self, architecture):
        self.db = torndb.Connection(
        host=options.mysql_host, database=options.mysql_database,
        user=options.mysql_user, password=options.mysql_password)

        architecturelow = architecture.lower()
        branch = ''
        hardware = ''

        lprofile = self.db.query('SELECT DISTINCT profile from crosswalk.reportsummary ORDER BY build_id DESC')
        larchitecture = self.db.query('SELECT DISTINCT darchitecture from crosswalk.reportsummary WHERE profile="android" ORDER BY build_id DESC')
        lbranch = self.db.query('SELECT DISTINCT branch from crosswalk.reportsummary WHERE profile="android" AND darchitecture=%s ORDER BY build_id DESC', architecturelow)
        lhardware = self.db.query('SELECT DISTINCT hardware from crosswalk.reportsummary WHERE profile="android" AND darchitecture=%s ORDER BY build_id DESC', architecturelow)

        avar = globals()
        awvar = globals()
        tvar = globals()
        twvar = globals()
        m= 0
        mw= 0
        n = 0
        nw = 0
        l = []
        avar['mr%s' % m] = self.db.query('SELECT * from crosswalk.reportsummary WHERE profile = "android" AND branch = "canary" AND hardware = "feature" ORDER BY build_id DESC, qa_id DESC LIMIT 16')
        if not avar['mr%s' % m] : raise tornado.web.HTTPError(404)
        m = m + 1 
        awvar['mrw%s' % mw] = self.db.query('SELECT * from crosswalk.reportsummary WHERE profile = "android" AND branch = "canary" AND hardware = "webapi" ORDER BY build_id DESC, qa_id DESC LIMIT 16')
        if not awvar['mrw%s' % mw] : raise tornado.web.HTTPError(404)
        mw = mw + 1 
        tvar['nr%s' % n] = self.db.query('SELECT * from crosswalk.reportsummary WHERE profile = "tizen" AND branch = "canary" AND hardware = "feature" ORDER BY build_id DESC, qa_id DESC LIMIT 16')
        if not tvar['nr%s' % n] : raise tornado.web.HTTPError(404)
        n = n + 1 
        twvar['nrw%s' % nw] = self.db.query('SELECT * from crosswalk.reportsummary WHERE profile = "tizen" AND branch = "canary" AND hardware = "webapi" ORDER BY build_id DESC, qa_id DESC LIMIT 16')
        if not twvar['nrw%s' % nw] : raise tornado.web.HTTPError(404)
        nw = nw + 1 
       
        for i in range(0, m):
            l.append(avar['mr%s' % i])
        for i in range(0, mw):
            l.append(avar['mrw%s' % i])
        for j in range(0, n):
            l.append(tvar['nr%s' % j])
        for j in range(0, nw):
            l.append(tvar['nrw%s' % j])
        self.render("report.htm", title="Crosswalk Nightly Test Report", l=l, platform='Android', architecture=architecture, branch=branch, hardware=hardware, lprofile=lprofile, larchitecture=larchitecture, lbranch=lbranch, lhardware=lhardware)

class ReportPlatformArchitectureAIAHandler(tornado.web.RequestHandler):
    def get(self, branch):
        self.db = torndb.Connection(
        host=options.mysql_host, database=options.mysql_database,
        user=options.mysql_user, password=options.mysql_password)

        branchlow = branch.lower()
        hardware = ''

        lprofile = self.db.query('SELECT DISTINCT profile from crosswalk.reportsummary ORDER BY build_id DESC')
        larchitecture = self.db.query('SELECT DISTINCT darchitecture from crosswalk.reportsummary WHERE profile="android" ORDER BY build_id DESC')
        lbranch = self.db.query('SELECT DISTINCT branch from crosswalk.reportsummary WHERE profile="android" AND darchitecture="ia" ORDER BY build_id DESC')
        lhardware = self.db.query('SELECT DISTINCT hardware from crosswalk.reportsummary WHERE profile="android" AND darchitecture="ia" AND branch=%s ORDER BY build_id DESC', branchlow)

        avar = globals()
        awvar = globals()
        tvar = globals()
        twvar = globals()
        m= 0
        mw= 0
        n = 0
        nw = 0
        l = []
        avar['mr%s' % m] = self.db.query('SELECT * from crosswalk.reportsummary WHERE profile = "android" AND branch = "canary" AND hardware = "feature" ORDER BY build_id DESC, qa_id DESC LIMIT 16')
        if not avar['mr%s' % m] : raise tornado.web.HTTPError(404)
        m = m + 1 
        awvar['mrw%s' % mw] = self.db.query('SELECT * from crosswalk.reportsummary WHERE profile = "android" AND branch = "canary" AND hardware = "webapi" ORDER BY build_id DESC, qa_id DESC LIMIT 16')
        if not awvar['mrw%s' % mw] : raise tornado.web.HTTPError(404)
        mw = mw + 1 
        tvar['nr%s' % n] = self.db.query('SELECT * from crosswalk.reportsummary WHERE profile = "tizen" AND branch = "canary" AND hardware = "feature" ORDER BY build_id DESC, qa_id DESC LIMIT 16')
        if not tvar['nr%s' % n] : raise tornado.web.HTTPError(404)
        n = n + 1 
        twvar['nrw%s' % nw] = self.db.query('SELECT * from crosswalk.reportsummary WHERE profile = "tizen" AND branch = "canary" AND hardware = "webapi" ORDER BY build_id DESC, qa_id DESC LIMIT 16')
        if not twvar['nrw%s' % nw] : raise tornado.web.HTTPError(404)
        nw = nw + 1 
       
        for i in range(0, m):
            l.append(avar['mr%s' % i])
        for i in range(0, mw):
            l.append(avar['mrw%s' % i])
        for j in range(0, n):
            l.append(tvar['nr%s' % j])
        for j in range(0, nw):
            l.append(tvar['nrw%s' % j])
        self.render("report.htm", title="Crosswalk Nightly Test Report", l=l, platform='Android', architecture='IA', branch=branch, hardware=hardware, lprofile=lprofile, larchitecture=larchitecture, lbranch=lbranch, lhardware=lhardware)

class ReportPlatformArchitectureAARMHandler(tornado.web.RequestHandler):
    def get(self, branch):
        self.db = torndb.Connection(
        host=options.mysql_host, database=options.mysql_database,
        user=options.mysql_user, password=options.mysql_password)

        branchlow = branch.lower()
        hardware = ''

        lprofile = self.db.query('SELECT DISTINCT profile from crosswalk.reportsummary ORDER BY build_id DESC')
        larchitecture = self.db.query('SELECT DISTINCT darchitecture from crosswalk.reportsummary WHERE profile="android" ORDER BY build_id DESC')
        lbranch = self.db.query('SELECT DISTINCT branch from crosswalk.reportsummary WHERE profile="android" AND darchitecture="arm" ORDER BY build_id DESC')
        lhardware = self.db.query('SELECT DISTINCT hardware from crosswalk.reportsummary WHERE profile="android" AND darchitecture="arm" AND branch=%s ORDER BY build_id DESC', branchlow)

        avar = globals()
        awvar = globals()
        tvar = globals()
        twvar = globals()
        m= 0
        mw= 0
        n = 0
        nw = 0
        l = []
        avar['mr%s' % m] = self.db.query('SELECT * from crosswalk.reportsummary WHERE profile = "android" AND branch = "canary" AND hardware = "feature" ORDER BY build_id DESC, qa_id DESC LIMIT 16')
        if not avar['mr%s' % m] : raise tornado.web.HTTPError(404)
        m = m + 1 
        awvar['mrw%s' % mw] = self.db.query('SELECT * from crosswalk.reportsummary WHERE profile = "android" AND branch = "canary" AND hardware = "webapi" ORDER BY build_id DESC, qa_id DESC LIMIT 16')
        if not awvar['mrw%s' % mw] : raise tornado.web.HTTPError(404)
        mw = mw + 1 
        tvar['nr%s' % n] = self.db.query('SELECT * from crosswalk.reportsummary WHERE profile = "tizen" AND branch = "canary" AND hardware = "feature" ORDER BY build_id DESC, qa_id DESC LIMIT 16')
        if not tvar['nr%s' % n] : raise tornado.web.HTTPError(404)
        n = n + 1 
        twvar['nrw%s' % nw] = self.db.query('SELECT * from crosswalk.reportsummary WHERE profile = "tizen" AND branch = "canary" AND hardware = "webapi" ORDER BY build_id DESC, qa_id DESC LIMIT 16')
        if not twvar['nrw%s' % nw] : raise tornado.web.HTTPError(404)
        nw = nw + 1 
       
        for i in range(0, m):
            l.append(avar['mr%s' % i])
        for i in range(0, mw):
            l.append(avar['mrw%s' % i])
        for j in range(0, n):
            l.append(tvar['nr%s' % j])
        for j in range(0, nw):
            l.append(tvar['nrw%s' % j])
        self.render("report.htm", title="Crosswalk Nightly Test Report", l=l, platform='Android', architecture='ARM', branch=branch, hardware=hardware, lprofile=lprofile, larchitecture=larchitecture, lbranch=lbranch, lhardware=lhardware)

    

class ReportPlatformArchitectureTHandler(tornado.web.RequestHandler):
    def get(self, architecture):
        self.db = torndb.Connection(
        host=options.mysql_host, database=options.mysql_database,
        user=options.mysql_user, password=options.mysql_password)

        architecturelow = architecture.lower()
        branch = ''
        hardware = ''

        lprofile = self.db.query('SELECT DISTINCT profile from crosswalk.reportsummary ORDER BY build_id DESC')
        larchitecture = self.db.query('SELECT DISTINCT darchitecture from crosswalk.reportsummary WHERE profile="tizen" ORDER BY build_id DESC')
        lbranch = self.db.query('SELECT DISTINCT branch from crosswalk.reportsummary WHERE profile="tizen" AND darchitecture=%s ORDER BY build_id DESC', architecturelow)
        lhardware = self.db.query('SELECT DISTINCT hardware from crosswalk.reportsummary WHERE profile="tizen" AND darchitecture=%s ORDER BY build_id DESC', architecturelow)

        avar = globals()
        awvar = globals()
        tvar = globals()
        twvar = globals()
        m= 0
        mw= 0
        n = 0
        nw = 0
        l = []
        avar['mr%s' % m] = self.db.query('SELECT * from crosswalk.reportsummary WHERE profile = "android" AND branch = "canary" AND hardware = "feature" ORDER BY build_id DESC, qa_id DESC LIMIT 16')
        if not avar['mr%s' % m] : raise tornado.web.HTTPError(404)
        m = m + 1 
        awvar['mrw%s' % mw] = self.db.query('SELECT * from crosswalk.reportsummary WHERE profile = "android" AND branch = "canary" AND hardware = "webapi" ORDER BY build_id DESC, qa_id DESC LIMIT 16')
        if not awvar['mrw%s' % mw] : raise tornado.web.HTTPError(404)
        mw = mw + 1 
        tvar['nr%s' % n] = self.db.query('SELECT * from crosswalk.reportsummary WHERE profile = "tizen" AND branch = "canary" AND hardware = "feature" ORDER BY build_id DESC, qa_id DESC LIMIT 16')
        if not tvar['nr%s' % n] : raise tornado.web.HTTPError(404)
        n = n + 1 
        twvar['nrw%s' % nw] = self.db.query('SELECT * from crosswalk.reportsummary WHERE profile = "tizen" AND branch = "canary" AND hardware = "webapi" ORDER BY build_id DESC, qa_id DESC LIMIT 16')
        if not twvar['nrw%s' % nw] : raise tornado.web.HTTPError(404)
        nw = nw + 1 
       
        for i in range(0, m):
            l.append(avar['mr%s' % i])
        for i in range(0, mw):
            l.append(avar['mrw%s' % i])
        for j in range(0, n):
            l.append(tvar['nr%s' % j])
        for j in range(0, nw):
            l.append(tvar['nrw%s' % j])
        self.render("report.htm", title="Crosswalk Nightly Test Report", l=l, platform='Tizen', architecture=architecture, branch=branch, hardware=hardware, lprofile=lprofile, larchitecture=larchitecture, lbranch=lbranch, lhardware=lhardware)

class ReportPlatformArchitectureTGenericHandler(tornado.web.RequestHandler):
    def get(self, branch):
        self.db = torndb.Connection(
        host=options.mysql_host, database=options.mysql_database,
        user=options.mysql_user, password=options.mysql_password)

        branchlow = branch.lower()
        hardware = ''

        lprofile = self.db.query('SELECT DISTINCT profile from crosswalk.reportsummary ORDER BY build_id DESC')
        larchitecture = self.db.query('SELECT DISTINCT darchitecture from crosswalk.reportsummary WHERE profile="tizen" ORDER BY build_id DESC')
        lbranch = self.db.query('SELECT DISTINCT branch from crosswalk.reportsummary WHERE profile="tizen" AND darchitecture="generic" ORDER BY build_id DESC')
        lhardware = self.db.query('SELECT DISTINCT hardware from crosswalk.reportsummary WHERE profile="tizen" AND darchitecture="generic" AND branch=%s ORDER BY build_id DESC', branchlow)

        avar = globals()
        awvar = globals()
        tvar = globals()
        twvar = globals()
        m= 0
        mw= 0
        n = 0
        nw = 0
        l = []
        avar['mr%s' % m] = self.db.query('SELECT * from crosswalk.reportsummary WHERE profile = "android" AND branch = "canary" AND hardware = "feature" ORDER BY build_id DESC, qa_id DESC LIMIT 16')
        if not avar['mr%s' % m] : raise tornado.web.HTTPError(404)
        m = m + 1 
        awvar['mrw%s' % mw] = self.db.query('SELECT * from crosswalk.reportsummary WHERE profile = "android" AND branch = "canary" AND hardware = "webapi" ORDER BY build_id DESC, qa_id DESC LIMIT 16')
        if not awvar['mrw%s' % mw] : raise tornado.web.HTTPError(404)
        mw = mw + 1 
        tvar['nr%s' % n] = self.db.query('SELECT * from crosswalk.reportsummary WHERE profile = "tizen" AND branch = "canary" AND hardware = "feature" ORDER BY build_id DESC, qa_id DESC LIMIT 16')
        if not tvar['nr%s' % n] : raise tornado.web.HTTPError(404)
        n = n + 1 
        twvar['nrw%s' % nw] = self.db.query('SELECT * from crosswalk.reportsummary WHERE profile = "tizen" AND branch = "canary" AND hardware = "webapi" ORDER BY build_id DESC, qa_id DESC LIMIT 16')
        if not twvar['nrw%s' % nw] : raise tornado.web.HTTPError(404)
        nw = nw + 1 
       
        for i in range(0, m):
            l.append(avar['mr%s' % i])
        for i in range(0, mw):
            l.append(avar['mrw%s' % i])
        for j in range(0, n):
            l.append(tvar['nr%s' % j])
        for j in range(0, nw):
            l.append(tvar['nrw%s' % j])
        self.render("report.htm", title="Crosswalk Nightly Test Report", l=l, platform='Tizen', architecture='Generic', branch=branch, hardware=hardware, lprofile=lprofile, larchitecture=larchitecture, lbranch=lbranch, lhardware=lhardware)

class ReportPlatformArchitectureTCommonHandler(tornado.web.RequestHandler):
    def get(self, branch):
        self.db = torndb.Connection(
        host=options.mysql_host, database=options.mysql_database,
        user=options.mysql_user, password=options.mysql_password)

        branchlow = branch.lower()
        hardware = ''

        lprofile = self.db.query('SELECT DISTINCT profile from crosswalk.reportsummary ORDER BY build_id DESC')
        larchitecture = self.db.query('SELECT DISTINCT darchitecture from crosswalk.reportsummary WHERE profile="tizen" ORDER BY build_id DESC')
        lbranch = self.db.query('SELECT DISTINCT branch from crosswalk.reportsummary WHERE profile="tizen" AND darchitecture="common" ORDER BY build_id DESC')
        lhardware = self.db.query('SELECT DISTINCT hardware from crosswalk.reportsummary WHERE profile="tizen" AND darchitecture="common" AND branch=%s ORDER BY build_id DESC', branchlow)

        avar = globals()
        awvar = globals()
        tvar = globals()
        twvar = globals()
        m= 0
        mw= 0
        n = 0
        nw = 0
        l = []
        avar['mr%s' % m] = self.db.query('SELECT * from crosswalk.reportsummary WHERE profile = "android" AND branch = "canary" AND hardware = "feature" ORDER BY build_id DESC, qa_id DESC LIMIT 16')
        if not avar['mr%s' % m] : raise tornado.web.HTTPError(404)
        m = m + 1 
        awvar['mrw%s' % mw] = self.db.query('SELECT * from crosswalk.reportsummary WHERE profile = "android" AND branch = "canary" AND hardware = "webapi" ORDER BY build_id DESC, qa_id DESC LIMIT 16')
        if not awvar['mrw%s' % mw] : raise tornado.web.HTTPError(404)
        mw = mw + 1 
        tvar['nr%s' % n] = self.db.query('SELECT * from crosswalk.reportsummary WHERE profile = "tizen" AND branch = "canary" AND hardware = "feature" ORDER BY build_id DESC, qa_id DESC LIMIT 16')
        if not tvar['nr%s' % n] : raise tornado.web.HTTPError(404)
        n = n + 1 
        twvar['nrw%s' % nw] = self.db.query('SELECT * from crosswalk.reportsummary WHERE profile = "tizen" AND branch = "canary" AND hardware = "webapi" ORDER BY build_id DESC, qa_id DESC LIMIT 16')
        if not twvar['nrw%s' % nw] : raise tornado.web.HTTPError(404)
        nw = nw + 1 
       
        for i in range(0, m):
            l.append(avar['mr%s' % i])
        for i in range(0, mw):
            l.append(avar['mrw%s' % i])
        for j in range(0, n):
            l.append(tvar['nr%s' % j])
        for j in range(0, nw):
            l.append(tvar['nrw%s' % j])
        self.render("report.htm", title="Crosswalk Nightly Test Report", l=l, platform='Tizen', architecture='Common', branch=branch, hardware=hardware, lprofile=lprofile, larchitecture=larchitecture, lbranch=lbranch, lhardware=lhardware)

class ReportPlatformArchitectureTIVIHandler(tornado.web.RequestHandler):
    def get(self, branch):
        self.db = torndb.Connection(
        host=options.mysql_host, database=options.mysql_database,
        user=options.mysql_user, password=options.mysql_password)

        branchlow = branch.lower()
        hardware = ''

        lprofile = self.db.query('SELECT DISTINCT profile from crosswalk.reportsummary ORDER BY build_id DESC')
        larchitecture = self.db.query('SELECT DISTINCT darchitecture from crosswalk.reportsummary WHERE profile="tizen" ORDER BY build_id DESC')
        lbranch = self.db.query('SELECT DISTINCT branch from crosswalk.reportsummary WHERE profile="tizen" AND darchitecture="ivi" ORDER BY build_id DESC')
        lhardware = self.db.query('SELECT DISTINCT hardware from crosswalk.reportsummary WHERE profile="tizen" AND darchitecture="ivi" AND branch=%s ORDER BY build_id DESC', branchlow)

        avar = globals()
        awvar = globals()
        tvar = globals()
        twvar = globals()
        m= 0
        mw= 0
        n = 0
        nw = 0
        l = []
        avar['mr%s' % m] = self.db.query('SELECT * from crosswalk.reportsummary WHERE profile = "android" AND branch = "canary" AND hardware = "feature" ORDER BY build_id DESC, qa_id DESC LIMIT 16')
        if not avar['mr%s' % m] : raise tornado.web.HTTPError(404)
        m = m + 1 
        awvar['mrw%s' % mw] = self.db.query('SELECT * from crosswalk.reportsummary WHERE profile = "android" AND branch = "canary" AND hardware = "webapi" ORDER BY build_id DESC, qa_id DESC LIMIT 16')
        if not awvar['mrw%s' % mw] : raise tornado.web.HTTPError(404)
        mw = mw + 1 
        tvar['nr%s' % n] = self.db.query('SELECT * from crosswalk.reportsummary WHERE profile = "tizen" AND branch = "canary" AND hardware = "feature" ORDER BY build_id DESC, qa_id DESC LIMIT 16')
        if not tvar['nr%s' % n] : raise tornado.web.HTTPError(404)
        n = n + 1 
        twvar['nrw%s' % nw] = self.db.query('SELECT * from crosswalk.reportsummary WHERE profile = "tizen" AND branch = "canary" AND hardware = "webapi" ORDER BY build_id DESC, qa_id DESC LIMIT 16')
        if not twvar['nrw%s' % nw] : raise tornado.web.HTTPError(404)
        nw = nw + 1 
       
        for i in range(0, m):
            l.append(avar['mr%s' % i])
        for i in range(0, mw):
            l.append(avar['mrw%s' % i])
        for j in range(0, n):
            l.append(tvar['nr%s' % j])
        for j in range(0, nw):
            l.append(tvar['nrw%s' % j])
        self.render("report.htm", title="Crosswalk Nightly Test Report", l=l, platform='Tizen', architecture='IVI', branch=branch, hardware=hardware, lprofile=lprofile, larchitecture=larchitecture, lbranch=lbranch, lhardware=lhardware)

class ReportCustomizeHandler(tornado.web.RequestHandler):
    def get(self, profile, architecture, branch, hardware):
        self.db = torndb.Connection(
        host=options.mysql_host, database=options.mysql_database,
        user=options.mysql_user, password=options.mysql_password)

        lprofile = self.db.query('SELECT DISTINCT profile from crosswalk.reportsummary ORDER BY build_id DESC')
        larchitecture = self.db.query('SELECT DISTINCT darchitecture from crosswalk.reportsummary WHERE profile=%s ORDER BY build_id DESC', profile)
        lbranch = self.db.query('SELECT DISTINCT branch from crosswalk.reportsummary WHERE profile=%s AND darchitecture=%s ORDER BY build_id DESC', profile, architecture)
        lhardware = self.db.query('SELECT DISTINCT hardware from crosswalk.reportsummary WHERE profile=%s AND darchitecture=%s AND branch=%s ORDER BY build_id DESC', profile, architecture, branch)

        avar = globals()
        awvar = globals()
        tvar = globals()
        twvar = globals()
        m= 0
        mw= 0
        n = 0
        nw = 0
        l = []
        avar['mr%s' % m] = self.db.query('SELECT * from crosswalk.reportsummary WHERE profile = "android" AND branch = "canary" AND hardware = "feature" ORDER BY build_id DESC, qa_id DESC LIMIT 16')
        if not avar['mr%s' % m] : raise tornado.web.HTTPError(404)
        m = m + 1 
        awvar['mrw%s' % mw] = self.db.query('SELECT * from crosswalk.reportsummary WHERE profile = "android" AND branch = "canary" AND hardware = "webapi" ORDER BY build_id DESC, qa_id DESC LIMIT 16')
        if not awvar['mrw%s' % mw] : raise tornado.web.HTTPError(404)
        mw = mw + 1 
        tvar['nr%s' % n] = self.db.query('SELECT * from crosswalk.reportsummary WHERE profile = "tizen" AND branch = "canary" AND hardware = "feature" ORDER BY build_id DESC, qa_id DESC LIMIT 16')
        if not tvar['nr%s' % n] : raise tornado.web.HTTPError(404)
        n = n + 1 
        twvar['nrw%s' % nw] = self.db.query('SELECT * from crosswalk.reportsummary WHERE profile = "tizen" AND branch = "canary" AND hardware = "webapi" ORDER BY build_id DESC, qa_id DESC LIMIT 16')
        if not twvar['nrw%s' % nw] : raise tornado.web.HTTPError(404)
        nw = nw + 1 
       
        for i in range(0, m):
            l.append(avar['mr%s' % i])
        for i in range(0, mw):
            l.append(avar['mrw%s' % i])
        for j in range(0, n):
            l.append(tvar['nr%s' % j])
        for j in range(0, nw):
            l.append(tvar['nrw%s' % j])
        self.render("report.htm", title="Crosswalk Nightly Test Report", l=l, platform=profile, architecture=architecture, branch=branch, hardware=hardware, lprofile=lprofile, larchitecture=larchitecture, lbranch=lbranch, lhardware=lhardware)

         
class ReportDetailHandler(tornado.web.RequestHandler):
    def get(self, entry_id):
        entries = ['x', 'xx', 'xxx']
        entry = entries[int(entry_id)]
        if not entries: raise tornado.web.HTTPError(404)
        self.render("reportdetail.htm", title="Crosswalk Test Report", entries=entries, entry=entry)
