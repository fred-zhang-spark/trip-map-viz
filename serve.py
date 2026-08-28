"""Tiny static server for the trip map. Run: python3 serve.py, then open http://localhost:8642"""
import os
os.chdir("/Users/fredzhang/Documents/Trip route and memory collection")
import http.server
import socketserver

PORT = 8642

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.allow_reuse_address = True
    print(f"Serving at http://localhost:{PORT}")
    httpd.serve_forever()
