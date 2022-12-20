import socket
from http.server import HTTPServer, BaseHTTPRequestHandler
class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content_type','text/html')
        self.end_headers()
        try:
            self.wfile.write(open(self.path[1:]).read().encode('utf-8'))
        except UnicodeDecodeError:
            pass
        except FileNotFoundError:
            self.wfile.write("File Not Found".encode('utf-8'))

 
            
port=8080
#_server=socket.gethostbyname(socket.gethostname())
_server='0.0.0.0'
server=HTTPServer((_server,port),handler)
print(f'Server running on port: {port}\nURL: http://{_server}:{port}/')
server.serve_forever() 