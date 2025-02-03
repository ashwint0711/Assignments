from http.server import BaseHTTPRequestHandler, HTTPServer

class CustomRequestHandler(BaseHTTPRequestHandler):
    #This will handle GET requests with a normal(Default) header.
    def do_GET(self):
        if self.path == "/api/data":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.send_header("Access-Control-Allow-Origin","*")
            self.send_header("Access-Control-Allow-Methods", "GET")
            self.end_headers()
            self.wfile.write(b'Hello from Data server\n')
        else:
            self.send_response(404)
    
    #When any request arrives with custom header this method will handle it
    #do_OPTIONS only handles "preflight" requests : 
        #After response from this method normal methods eg do_GET or do_POST gets called 
        #and rest is handled by respective methods.
    def do_OPTIONS(self):  # Handle preflight requests
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "http://localhost:7000")
        self.send_header("Access-Control-Allow-Methods", "GET")
        #If a GET request contains "Content-Type" header then server has to allow that
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()



if __name__ == "__main__":
    server_address = ('0.0.0.0', 5000) #Allow localhost requets
    httpd = HTTPServer(server_address, CustomRequestHandler)

    httpd.serve_forever()