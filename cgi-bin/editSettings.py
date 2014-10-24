#!/usr/bin/python

import cgi
import datetime
import cgitb
import os 
import Cookie
import sqlite3
cgitb.enable()

t = str(datetime.datetime.now())
form = cgi.FieldStorage()
cookie_string = os.environ.get('HTTP_COOKIE')

conn = sqlite3.connect('BESTOS_DATABASE.db')
c = conn.cursor()

def main():
	print "Content-type: text/html"
	print
	

main()