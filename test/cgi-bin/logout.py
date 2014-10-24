#!/usr/bin/python

import cgi
import cgitb
import sqlite3
cgitb.enable()

form = cgi.FieldStorage()

conn = sqlite3.connect('BESTOS_DATABASE.db')

def main():
	sID = form['sid'].value
	print """Content-type: text/html

<html><head><title>Logout</title></head><body>
<p>You are now logged out. Return to <a href = "http://test.elin9.rochestercs.org/">home</a>.</p>
</body></html>"""
	logout(conn,sID)

def logout(conn, sID):
	c = conn.cursor()
	c.execute('update users set sessionID=0 where sessionID=?;',(sID,))
	conn.commit()
	conn.close()
	
main()