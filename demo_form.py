# -*- coding: utf-8 -*-
 
class MyFormHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('<html><body><form action="/form" method="post">'
                   '<input type="text" name="message">'
                   '<input type="submit" value="Submit">'
                   '</form></body></html>')

    def post(self):
        self.set_header("Content-Type", "text/html")
        self.write("You wrote " + self.get_argument("message"))

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/asyc", AsycHandler),
    (r"/crosswalk/android/canary/([0-9]+)", CrosswalkAndroidCanaryBuildHandler),
    (r"/form", MyFormHandler),
])


 
 