from http.server import BaseHTTPRequestHandler, HTTPServer

class CustomeRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/ping":
            self.send_response(200)
            self.end_headers()

            self.wfile.write("pong\n".encode("utf-8"))
        else:
            self.send_response(400)
            self.end_headers()
            
            self.wfile.write("Invalid request!\n".encode("utf-8"))


if __name__ == "__main__":
    server_address = ('0.0.0.0', 5001)
    httpd = HTTPServer(server_address, CustomeRequestHandler)

    httpd.serve_forever()
