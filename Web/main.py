import os
import re
import json

import tornado.auth
import tornado.httpserver
import tornado.ioloop
import tornado.web
import torndb

import nltk
from nltk.corpus import wordnet as wn

from tornado.options import options, define

define("port", default="8080")
define("mysql_host", default="127.0.0.1:3306")
define("mysql_database", default="saxons")
define("mysql_user", default="root")
define("mysql_password", default="creativekit")


'''
,

            (r"/help", FeedHandler),
            (r"/setting", SettingHandler),
            (r"/auth/login", AuthLoginHandler),
            (r"/auth/logout", AuthLogoutHandler),
'''


class Application(tornado.web.Application):
	def __init__(self):
		handlers = [
			(r"/", EntryHandler),
			(r"/getword", LangPackBrowseHandler),
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

		self.db = torndb.Connection(
			host=options.mysql_host, database=options.mysql_database,
			user=options.mysql_user, password=options.mysql_password)

		
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
		self.render("main.html", user=self.current_user)


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
self.db.query("select * ")
self.render("settings.html")
'''
			pass

class LangPackBrowseHandler(tornado.web.RequestHandler):
	def get(self):
		return_list = []
		for pack in self.application.db.query("select * from public_lang_pack"):
			return_list.append({'name': pack.name,
								'publish_date': pack.publish_date,
								'lang_type': pack.lang_type,
								'description': pack.description})
		self.write(str(return_list))


def main():
	options.parse_command_line()
	http_server = tornado.httpserver.HTTPServer(Application())
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
	main()