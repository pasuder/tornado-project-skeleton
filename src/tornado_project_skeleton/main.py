import os
import tornado.autoreload
import tornado.ioloop
import tornado.web

from tornado_project_skeleton.tools import config


pwd = os.path.dirname(os.path.abspath(__file__))
config.add_config_ini('%s/main.ini' % pwd)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        name = config.NAME
        items = ['smart', 'clever', 'intuitive']
        kwargs = {'title': 'My title',
                  'name': name,
                  'items': items}
        self.render('template.html', **kwargs)

    def data_received(self, chunk):
        pass


application = tornado.web.Application(
    handlers=[
        (r'/', MainHandler),
        (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': '%s/static/' % pwd}),
    ])

if __name__ == "__main__":
    application.listen(8888)
    tornado.autoreload.start()
    tornado.autoreload.watch('%s/template.html' % pwd)
    tornado.autoreload.watch('%s/static/style.css' % pwd)
    tornado.ioloop.IOLoop.instance().start()
