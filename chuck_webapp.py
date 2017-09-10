#! /usr/bin/env python3

import logging
import tornado.ioloop
import tornado.web


log = logging.getLogger(__name__)
log.addHandler(logging.StreamHandler())
log.addHandler(logging.FileHandler(filename=__name__+'.log'))
log.setLevel(logging.DEBUG)


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
    ], log_function=log.info)


def main():

    import os
    import signal
    import sys



    log.info('PID is {}'.format(os.getpid()))

    loop = tornado.ioloop.IOLoop.current()

    def siggie(signum, _):
        log.info('Recieved signal {}, shutting down...'.format(signum))
        loop.add_callback_from_signal(loop.stop)
    signal.signal(signal.SIGINT, siggie)
    signal.signal(signal.SIGTERM, siggie)

    app = make_app()
    try:
        app.listen(80)
    except PermissionError:
        log.exception('Cannot bind socket 80, needed for CHUCK WEBAPP. Try again with sudo?')
        sys.exit(1)
    log.info('Created CHUCK WEBAPP. Starting loop...')

    loop.start()
    log.info('We hope you enjoyed CHUCK WEBAPP. Byebye!')


if __name__ == "__main__":
    main()
