from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import os

PORT = 8000

class FileListingHandler(SimpleHTTPRequestHandler):
    def list_directory(self, path):
        files = sorted(os.listdir(path))

        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>File Listing</title>
        </head>
        <body>
            <h1>Files</h1>
            <ul>
        """

        for filename in files:
            if filename.startswith("."):
                continue

            url = "/" + filename.replace("\\", "/")
            html += f'<li><a href="{url}">{filename}</a></li>'

        html += """
            </ul>
        </body>
        </html>
        """

        data = html.encode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

server = ThreadingHTTPServer(("localhost", PORT), FileListingHandler)

print(f"Serving directory at http://localhost:{PORT}/")
server.serve_forever()

