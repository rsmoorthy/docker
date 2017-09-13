#!/usr/bin/python

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import subprocess
import os
import pql
import json

class S(BaseHTTPRequestHandler, object):

  def __init__(self, *args, **kwargs):
    self.parser = pql.SchemaFreeParser()
    super(S, self).__init__( *args, **kwargs )

  def run(self, cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, close_fds=True)
    out, err = p.communicate()
    return out

  def process(self, path, q):
    if path == 'expr2mongo':
      if not ('expr' in q):
        return "error: invalid parameters passed".encode()
      return json.dumps(self.parser.parse(q['expr'][0])).encode()
    return 'error: invalid method'.encode()

  def _set_headers(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()


  def do_GET(self):
    self._set_headers()
    query = parse_qs(urlparse(self.path).query)
    path = urlparse(self.path).path[1:]
    if path.endswith('/'):
      path = path[:-1]
    self.wfile.write(self.process(path, query))

  def do_HEAD(self):
    self._set_headers()

  def do_POST(self):
    # Doesn't do anything with posted data
    self._set_headers()
    length = int(self.headers.get('content-length'))
    field_data = self.rfile.read(length).decode('utf-8')
    query = parse_qs(field_data)
    path = urlparse(self.path).path[1:]
    if path.endswith('/'):
      path = path[:-1]
    self.wfile.write(self.process(path, query))

def start(server_class=HTTPServer, handler_class=S, port=80):
  server_address = ('', port)
  httpd = server_class(server_address, handler_class)
  print('Starting httpd...')
  httpd.serve_forever()

if __name__ == "__main__":
  from sys import argv

  if len(argv) == 2:
    start(port=int(argv[1]))
  else:
    start()
