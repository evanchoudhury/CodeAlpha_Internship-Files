import os
import tempfile
import http.server
import socketserver
import threading
import time
from scrape_title import scrape_title

PORT = 8000

class TestHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/notitle":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"<html><body>No title here</body></html>")
        else:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"<html><head><title>Test Title</title></head><body>Hello</body></html>")

def run_test_server():
    with socketserver.TCPServer(("", PORT), TestHTTPRequestHandler) as httpd:
        httpd.serve_forever()

def test_scrape_title_valid():
    with tempfile.TemporaryDirectory() as tmpdir:
        output_path = os.path.join(tmpdir, "title.txt")
        url = f"http://localhost:{PORT}/"
        scrape_title(url, output_path)
        with open(output_path, 'r', encoding='utf-8') as f:
            title = f.read().strip()
        assert title == "Test Title"

def test_scrape_title_no_title():
    with tempfile.TemporaryDirectory() as tmpdir:
        output_path = os.path.join(tmpdir, "title.txt")
        url = f"http://localhost:{PORT}/notitle"
        scrape_title(url, output_path)
        assert not os.path.exists(output_path) or os.path.getsize(output_path) == 0

def test_scrape_title_invalid_url():
    with tempfile.TemporaryDirectory() as tmpdir:
        output_path = os.path.join(tmpdir, "title.txt")
        url = "http://localhost:9999/invalid"
        scrape_title(url, output_path)
        assert not os.path.exists(output_path) or os.path.getsize(output_path) == 0

if __name__ == "__main__":
    server_thread = threading.Thread(target=run_test_server, daemon=True)
    server_thread.start()
    time.sleep(1)  # Wait for server to start

    test_scrape_title_valid()
    test_scrape_title_no_title()
    test_scrape_title_invalid_url()

    print("All scrape_title tests passed.")
