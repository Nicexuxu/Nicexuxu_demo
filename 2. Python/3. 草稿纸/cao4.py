from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 设置响应状态码为200（OK）
        self.send_response(200)
        
        # 设置响应头，指定内容类型为 HTML
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        # 自定义 HTML 页面内容
        html_content = """
        <html>
            <head><title>My Custom Page</title></head>
            <body>
                <h1>Welcome to My Custom Server!</h1>
                <p>This is a simple HTML page served by Python.</p>
            </body>
        </html>
        """
        
        # 将 HTML 内容发送到客户端
        self.wfile.write(html_content.encode('utf-8'))

def run(server_class=HTTPServer, handler_class=MyHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
