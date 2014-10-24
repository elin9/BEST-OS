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
	all_results = []
	cookieIsWorking = True
	
	if cookie_string:  #if user is already logged in
		aCookie = Cookie.SimpleCookie(cookie_string)
		try:
			savedSID = aCookie['sessionID'].value
			c.execute('select * from users where sessionID=?', (savedSID,))
			all_results = c.fetchall()
		except:
			cookieIsWorking = False
			print 
	        	print "<html><head><title>Login</title></head>"
	        	print "<body>"
	        	print 'An error occurred. Try deleting your stored cookies for this site, then <a href ="http://elin9.rochestercs.org/cgi-bin/login.py">try again</a>.<br><br>'
	        	print "</body></html>"
		
	if len(all_results) > 0:
		savedName = all_results[0][0]
	 	print 
	        print "<html><head><title>Login</title></head>"
	        print "<body>"
	        print "<h1>Welcome back, " + savedName + "!</h1>"
	        print "<h2> I already have your cookie. </h2>"
		print "<h2> Last login time: " + aCookie['current_time'].value + "</h2><br>"
		print '<h2>Go <a href="http://elin9.rochestercs.org/experimenting">here</a> to homepage.</h2>'
		print '<form method = post action = "logout.py">'
		print '<input type = hidden name = "sid" value = ' + str(savedSID) + '>'
		print '<input type=submit name = "logout" value = "Logout">' #logout button here
		print "</form>"
	        
	else:	#if user is just logging in
		if cookieIsWorking:  
			
			formName = form.getvalue("username")
			formPass = form.getvalue("password")
			
			if formName == None:
				print """
					<html>
					<head>
					<title> Login </title> 
					<head>
					<body>
					
					<form method="post" action="login.py">
					
					<fieldset>
					<legend>Please enter your username and password to login:</legend>
					Username: <input name="username" type=text size="20" required/><br>
					Password: <input name="password" type=password size="20" required/><br>
					<input type="Submit"/>
					</fieldset>
					
					</form>
					<br>
					Return to <a href="http://elin9.rochestercs.org">home</a>.
					</body>
					</html>
				"""
			else:
				
				dbName = checkUsername(c, formName)
				if formName == dbName:          #if username entered is in database
					dbPass = checkPassword(c, dbName)
					if formPass == dbPass:  #if password entered matches the one in the database
					        import uuid
					        sessionID = str(uuid.uuid4())
					        c.execute('update users set sessionID=? where username=?', (sessionID, dbName))
					        conn.commit()
					        
					        aCookie = Cookie.SimpleCookie()
					        aCookie['name'] = "login"
					        aCookie['sessionID'] = sessionID
					        #aCookie['sessionID']['path'] = "/"
					        aCookie['current_time'] = t
					        expires = datetime.datetime.now() + datetime.timedelta(days=7) #cookie expires in 7 days
					        aCookie['sessionID']['expires'] = expires.strftime("%a, %d %b %Y %H:%M:%S GMT")
					        aCookie['current_time']['expires'] = expires.strftime("%a, %d %b %Y %H:%M:%S GMT")
					        
					        
					        print aCookie
					        print 
					        print "<html><head><title>Login</title></head>"
					        print "<body>"
					        print "<h1>Hi, " + dbName + "! You are now logged in. Also sent you a cookie. Yum.</h1>"
						print "<h2>Login time: " + aCookie['current_time'].value + "</h2>"
						print "<h2>SessionID: " + sessionID + "</h2>"
						print "<h2>Cookie Expiration: " + str(expires) + "</h2>"
						print '<h2>Go <a href="http://elin9.rochestercs.org/experimenting">here</a> to homepage.</h2>'
						print '<form method = post action = "logout.py">'
						print '<input type = hidden name = "sid" value = ' + str(sessionID) + '>'
						print '<input type=submit name = "logout" value = "Logout">' #logout button here
						print "</form>"
					else:  #if incorrect password
						print
						print "<html><head><title>Login</title></head><body>"
						print '<h1>Incorrect Password! <a href="http://elin9.rochestercs.org/cgi-bin/login.py">Try again.</a></h1>'
				else:  #if username entered is not in database
				        print 
				        print "<html><head><title>Login</title></head>"
				        print "<body>"
				        print "<h1>Sorry, you are not registered.</h1>"
				        print formName
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