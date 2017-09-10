#! /usr/bin/env python3

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('static/html/hi_chuck.html')

class BirthdayHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('static/html/birthday.html')

def make_app():
    return tornado.web.Application([
        #(r'/html', tornado.web.StaticFileHandler, {'path' : 'static/html',}),
        (r'/imgs/(.*)', tornado.web.StaticFileHandler, {'path' : 'static/imgs',}),
        (r"/birthday", BirthdayHandler),
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    import signal

    loop = tornado.ioloop.IOLoop.current()

    def siggie(signum, _):
        print('Recieved signal {}, shutting down...'.format(signum))
        loop.add_callback_from_signal(loop.stop)
    signal.signal(signal.SIGINT, siggie)
    signal.signal(signal.SIGTERM, siggie)

    app = make_app()
    app.listen(8888)
    print('Created CHUCK WEBAPP. Starting loop...')

    loop.start()
    print('We hope you enjoyed CHUCK WEBAPP. Byebye!')