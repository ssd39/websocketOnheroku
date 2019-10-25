from tornado import websocket
import tornado.ioloop
import os

class EchoWebSocket(websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        print("Websocket Opened")

    def on_message(self, message):
        self.write_message(u"You said: %s" % message)

    def on_close(self):
        print("Websocket closed")

application = tornado.web.Application([(r"/", EchoWebSocket),])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    application.listen(port)
    tornado.ioloop.IOLoop.instance().start()