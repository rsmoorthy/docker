#!/usr/bin/python

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from urlparse import urlparse, parse_qs
import subprocess
import os
import typekeys

class S(BaseHTTPRequestHandler, object):

  def __init__(self, *args, **kwargs):
    super(S, self).__init__( *args, **kwargs )

  def run(self, cmd):
    print cmd
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, close_fds=True)
    out, err = p.communicate()
    return out

  def process(self, q):
    if not ('company' in q and 'username' in q and 'passwd' in q):
      return "error: invalid parameters passed"
    folderPath = q['folderPath'][0] if 'folderPath' in q  else ''
    out = self.run(["/root/sevents.sh", q['company'][0], q['username'][0], q['passwd'][0], folderPath])
    print out
    return 'ok'

  def _set_headers(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()


  def do_GET(self):
    self._set_headers()
    query = parse_qs(urlparse(self.path).query)
    path = urlparse(self.path).path
    print path
    print query
    self.wfile.write(self.process(query))

  def do_HEAD(self):
    self._set_headers()

  def do_POST(self):
    # Doesn't do anything with posted data
    self._set_headers()
    length = int(self.headers.getheader('content-length'))
    field_data = self.rfile.read(length)
    query = parse_qs(field_data)
    path = urlparse(self.path).path
    print path
    print query
    self.wfile.write(self.process(query))

def start(server_class=HTTPServer, handler_class=S, port=8080):
  server_address = ('', port)
  httpd = server_class(server_address, handler_class)
  print 'Starting httpd...'
  httpd.serve_forever()

if __name__ == "__main__":
  from sys import argv

  if len(argv) == 2:
    start(port=int(argv[1]))
  else:
    start()
