#!/usr/bin/python

import cgi
import cgitb
import sqlite3
import datetime
import os
import Cookie
import json
cgitb.enable()

form = cgi.FieldStorage()
cookie_string = os.environ.get('HTTP_COOKIE')

conn = sqlite3.connect('BESTOS_DATABASE.db')

def main():
	bookinfo = form.getvalue("info")
	
	print "Content-type: text/plain"
	print
	print bookinfo
	
main()