#!/usr/bin/python

import cgi
import cgitb
import sqlite3
import datetime
import os
import Cookie
cgitb.enable()

form = cgi.FieldStorage()
cookie_string = os.environ.get('HTTP_COOKIE')

conn = sqlite3.connect('BESTOS_DATABASE.db')

def main():
	sID = form['sid'].value
	print "Content-type: text/html"
	deleteCookie()
	print """
	
		<html><head><title>Logout</title></head><body>
		<p>You are now logged out. Return to <a href = "http://test.elin9.rochestercs.org/cgi-bin/index.php">home</a>.</p>
		</body></html>"""
	logout(conn,sID)

def logout(conn, sID):
	c = conn.cursor()
	c.execute('update users set sessionID=0 where sessionID=?;',(sID,))
	conn.commit()
	conn.close()
	
def deleteCookie( ):
	aCookie = Cookie.SimpleCookie(cookie_string)
	aCookie['name']['expires'] = 'Thu, 01 Jan 1970 00:00:00 GMT'
	aCookie['current_time']['expires'] = 'Thu, 01 Jan 1970 00:00:00 GMT'
	aCookie['sessionID']['expires'] = 'Thu, 01 Jan 1970 00:00:00 GMT'
	print aCookie
	
main()