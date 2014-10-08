#!/usr/bin/python

import cgi
import datetime
import cgitb
import os 
import Cookie
import sqlite3
import logging
cgitb.enable()

t = str(datetime.datetime.now())
form = cgi.FieldStorage()
cookie_string = os.environ.get('HTTP_COOKIE')

conn = sqlite3.connect('BESTOS_DATABASE.db')
c = conn.cursor()

def main():
	print "Content-type: text/html"
	if cookie_string:  #if user is already logged in
		aCookie = Cookie.SimpleCookie(cookie_string)
		savedSID = aCookie['sessionID'].value
	
		c.execute('select * from users where sessionID=?', (savedSID,))
		all_results = c.fetchall()
		if len(all_results) > 0:
			savedName = all_results[0][0]
		        print 
		        print "<html><head><title>Login</title></head>"
		        print "<body>"
		        print "<h1>Welcome back, " + savedName + "!</h1>"
			print "<h2>I already have your cookie. <br> Last login time: " + aCookie['current_time'].value + "</h2>"
		else:
		        print 
		        print "<html>"
		        print "<body>"
		        print "<h1>Imposter! SessionID Mismatch: Someone else has logged into your account.</h1>"
	        
	else:  #if user is just logging in
		formName = form['username'].value
		formPass = form['password'].value
		dbName = checkUsername(c, formName)
		
		if formName == dbName:          #if username entered is in database
			dbPass = checkPassword(c, dbName)
			if formPass == dbPass:  #if password entered matches the one in the database
			        import uuid
			        sessionID = str(uuid.uuid4())
			        c.execute('update users set sessionID=? where username=?', (sessionID, dbName))
			        conn.commit()
			        
			        aCookie = Cookie.SimpleCookie()
			        aCookie['sessionID'] = sessionID
			        aCookie['current_time'] = t
			        
			        print aCookie
			        print 
			        print "<html><head><title>Login</title></head>"
			        print "<body>"
			        print "<h1>Hi, " + dbName + "! You are now logged in. Also sent you a cookie. Yum.</h1>"
				print "<h2>Login time: " + aCookie['current_time'].value + "</h2>"
				print "<h2>SessionID: " + sessionID + "</h2>"
			else:  #if incorrect password
				print
				print "<html><head><title>Login</title></head><body>"
				print '<h1>Incorrect Password! <a href="http://elin9.rochestercs.org/login.html">Try again.</a></h1>'
		else:  #if username entered is not in database
		        print 
		        print "<html><head><title>Login</title></head>"
		        print "<body>"
		        print "<h1>Sorry, you are not registered.</h1>"
		        print '<h2>Go <a href="http://elin9.rochestercs.org/cgi-bin/form.py">here</a> to create an account.</h2>'
	print("</body></html>")

def sendCookie():  #not used
	aCookie = Cookie.SimpleCookie()
	aCookie['app_name'] = 'best-os'
	aCookie['current_time'] = t
	print(aCookie)

def checkUsername(c, variable):
	c.execute('select username from users where username = ?;',(variable,))
	n = str("%s" % c.fetchone())
	return n

def checkPassword(c, usrname):
	c.execute('select password from users where username = ?;',(usrname,))	
	p = str("%s" % c.fetchone())
	return p

main()