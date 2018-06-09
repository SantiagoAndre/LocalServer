import SimpleHTTPServer
import SocketServer

PORT = 8001
class MyHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
	def do_GET(self):
		if self.path == '/':
			self.path = '/design.html'
			return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
Handler = MyHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()
