#!/usr/bin/env python3
"""AniMotion local web server with a loopback-only ComfyUI reverse proxy."""
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from shutil import copyfileobj
import os
from pathlib import Path

HOST = "127.0.0.1"
PORT = 8090
COMFY = "http://127.0.0.1:8188"


class Handler(SimpleHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def _proxy(self):
        parsed = urlsplit(self.path)
        if not (parsed.path == "/comfy" or parsed.path.startswith("/comfy/")):
            return False
        remote_path = parsed.path[len("/comfy"):] or "/"
        target = COMFY + remote_path + (("?" + parsed.query) if parsed.query else "")
        body = None
        if self.command in ("POST", "PUT", "PATCH"):
            length = int(self.headers.get("Content-Length", "0"))
            body = self.rfile.read(length) if length else b""
        headers = {}
        for name in ("Content-Type", "Accept", "Range", "If-None-Match", "If-Modified-Since"):
            value = self.headers.get(name)
            if value:
                headers[name] = value
        req = Request(target, data=body, headers=headers, method=self.command)
        try:
            response = urlopen(req, timeout=1800)
            status = response.status
            response_headers = response.headers
            stream = response
        except HTTPError as exc:
            status = exc.code
            response_headers = exc.headers
            stream = exc
        except (URLError, TimeoutError, OSError) as exc:
            payload = ("ComfyUI is not reachable at 127.0.0.1:8188: " + str(exc)).encode("utf-8")
            self.send_response(502)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("Content-Length", str(len(payload)))
            self.end_headers()
            if self.command != "HEAD":
                self.wfile.write(payload)
            return True

        self.send_response(status)
        for name in ("Content-Type", "Content-Length", "Content-Disposition", "Accept-Ranges", "Content-Range", "Last-Modified", "ETag", "Cache-Control"):
            value = response_headers.get(name)
            if value:
                self.send_header(name, value)
        self.end_headers()
        if self.command != "HEAD":
            copyfileobj(stream, self.wfile, length=1024 * 1024)
        stream.close()
        return True

    def do_GET(self):
        if not self._proxy():
            super().do_GET()

    def do_HEAD(self):
        if not self._proxy():
            super().do_HEAD()

    def do_POST(self):
        if not self._proxy():
            self.send_error(404)

    def do_PUT(self):
        if not self._proxy():
            self.send_error(404)

    def do_PATCH(self):
        if not self._proxy():
            self.send_error(404)


if __name__ == "__main__":
    os.chdir(Path(__file__).resolve().parent)
    print(f"AniMotion Studio: http://{HOST}:{PORT}")
    print(f"Local ComfyUI proxy: http://{HOST}:{PORT}/comfy → {COMFY}")
    print("Only this computer can access the local web server. Press Ctrl+C to stop.")
    ThreadingHTTPServer((HOST, PORT), Handler).serve_forever()
