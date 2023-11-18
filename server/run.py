import http.server

class Server():
    def __init__(self, server_class=http.server.HTTPServer, handler_class=http.server.BaseHTTPRequestHandler):
        self.server_class = server_class
        self.handler_class = handler_class
    def start(self):
        server_address = ('', 8000)
        httpd = self.server_class(server_address, self.handler_class)
        httpd.serve_forever()