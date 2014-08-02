import os
import re

import tornado.auth
import tornado.httpserver
import tornado.ioloop
import tornado.options 
import tornado.web
import torndb

tornado.options.define("port", default="8080")


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", EntryHandler)
            
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
           # ui_modules={"Entry": EntryModule},
            xsrf_cookies=True,
            cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
            login_url="/auth/login",
            debug=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)
       

        "connect db"
        '''
        self.db = torndb.Connection(
            host=options.mysql_host, database=options.mysql_database,
            user=options.mysql_user, password=options.mysql_password)

        '''
class EntryHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("home.html")

class BaseHandler(tornado.web.RequestHandler):
    @property   
    def db(self):
        return self.application.db

    def get_current_user(self):
        return self.get_secret_cookie("userid")

    
class HomeHandler(BaseHandler):
    def get(self):
        self.render("mainpage.html", user = self.current_user)

        
class LearningProcessHandler(BaseHandler):
    def get(self):
        if not self.current_user:
            self.redirect("/")
            return
            
            
class SavePackHandler(BaseHandler):
    def get(self):
        if not self.current_user:
            self.redirect("/")
            return
        
class SettingHandler(BaseHandler):
    def get(self):
        if not self.current_user:
            self.redirect("/")
            return
        else:
            '''
            fetch db
            self.render("settings.html", user = 
            '''
            pass
    
    
    
    
    
    
    
def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()