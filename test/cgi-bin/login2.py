#!/usr/bin/python

import cgi
import datetime
import cgitb
import os 
import Cookie
import sqlite3
import uuid
cgitb.enable()

t = str(datetime.datetime.now())
form = cgi.FieldStorage()
cookie_string = os.environ.get('HTTP_COOKIE')

conn = sqlite3.connect('BESTOS_DATABASE.db')
c = conn.cursor()

def main():
	print "Content-type: text/html"

	formName = form.getvalue("username")
	formPass = form.getvalue("password")
			
	dbName = checkUsername(c, formName)
	if formName == dbName:          #if username entered is in database
		dbPass = checkPassword(c, dbName)
		if formPass == dbPass:  #if password entered matches the one in the database
			sessionID = str(uuid.uuid4())
			c.execute('update users set sessionID=? where username=?', (sessionID, dbName))
			conn.commit()
					        
			aCookie = Cookie.SimpleCookie()
			aCookie['name'] = formName
			aCookie['sessionID'] = sessionID
			aCookie['current_time'] = t
			expires = datetime.datetime.now() + datetime.timedelta(days=7) #cookie expires in 7 days
			aCookie['name']['expires'] = expires.strftime("%a, %d %b %Y %H:%M:%S GMT")
			aCookie['sessionID']['expires'] = expires.strftime("%a, %d %b %Y %H:%M:%S GMT")
			aCookie['current_time']['expires'] = expires.strftime("%a, %d %b %Y %H:%M:%S GMT")	        
					        
			print aCookie
			print
			print "<html><body>"
			print dbName
		else:  #if incorrect password
			print
			print "<html><body>"
			print "Incorrect Password! Try again."
	else:  #if username entered is not in database
		print 
		print "<html><body>"
		print "Sorry, you are not registered."
		print 'Go <a href="http://test.elin9.rochestercs.org/cgi-bin/form.py">here</a> to create an account.'
	print "</body></html>"
	
def checkUsername(c, variable):
	c.execute('select username from users where username = ?;',(variable,))
	n = str("%s" % c.fetchone())
	return n

def checkPassword(c, usrname):
	c.execute('select password from users where username = ?;',(usrname,))	
	p = str("%s" % c.fetchone())
	return p

main()