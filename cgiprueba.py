#!/usr/bin/python
import cgi
import SimpleHTTPServer
import SocketServer
PORT = 8001
class MyHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header("Context-type","text/html")
		self.end_headers()
		self.wfile.write('<html>')
		self.wfile.write('<head><title>My First CGI Program</title></head>')
		self.wfile.write('<body>')
		self.wfile.write('<h1>Hello Program!</h1>')
		form = cgi.FieldStorage()
		if form.getvalue("name"):
			name = form.getvalue("name")
			self.wfile.write('<h1>Hello ' + name + '! Thanks for using my script!</h1><br />')
		if form.getvalue("happy"):
			self.wfile.write("<p> Yay! I'm happy too! </p>")
		if form.getvalue("sad"):
			self.wfile.write("<p> Oh no! Why are you sad? </p>")
		self.wfile.write('<form method="post" action="cgiprueba.py">')
		self.wfile.write('<p>Name: <input type="text" name="name"/></p>')
		self.wfile.write('<input type="checkbox" name="happy" /> Happy')
		self.wfile.write('<input type="checkbox" name="sad" /> Sad')
		self.wfile.write('<input type="submit" value="Submit" />')
		self.wfile.write('</form>')
		self.wfile.write('</body>')
		self.wfile.write('</html>')





Handler = MyHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)
print "serving at port", PORT
httpd.serve_forever()
