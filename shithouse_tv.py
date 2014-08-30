#!/usr/bin/env python2

from bottle import route, run, template, request
import subprocess

@route("/")
def root():
    mheader = request.get_header("host")
    return subprocess.check_output(["luajit-2.0.0-beta9", "./src/root.lua"])

def main():
    run(host='localhost', port=8080)

if __name__ == '__main__':
    main()
