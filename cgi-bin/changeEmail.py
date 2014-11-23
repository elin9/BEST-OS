#!/usr/bin/python

import cgi
import cgitb
import os 
import Cookie
import sqlite3
cgitb.enable()

form = cgi.FieldStorage()
cookie_string = os.environ.get('HTTP_COOKIE')

conn = sqlite3.connect('BESTOS_DATABASE.db')
c = conn.cursor()

def main():
	if cookie_string:
		aCookie = Cookie.SimpleCookie(cookie_string)
		user = aCookie['name'].value 
		oldEmail = form.getvalue("oldEmail")
		newEmail = form.getvalue("newEmail")
		c.execute('select email from users where username = ?',(user,))
	   	dbEmail = str("%s" % c.fetchone())
	    	c.execute('select username from users where email = ?',(newEmail,))
	    	emailInDB = str("%s" % c.fetchone())

		print "Content-type: text/html"
		print
		print "<html><head><title>Change Email</title></head><body>"
		if oldEmail != dbEmail:
			print "The current email address you entered does not exist.<br>"
			changeEmailForm()
		elif str(emailInDB) != "None":
			print "An account already exists with this email.<br>"
			changeEmailForm()
			print "Return to <a href='http://elin9.rochestercs.org/cgi-bin/editSettingsTabs.py'>settings</a>."
		else:
			c.execute('update users set email = ? where username = ? and email = ?;', (newEmail, user, oldEmail))
			conn.commit()
			print "You have successfully changed your email address to " + str(newEmail) + "<br>"
			print "Return to <a href='http://elin9.rochestercs.org/cgi-bin/editSettingsTabs.py'>settings</a>."
		conn.close()
		print "</body></html>"

def changeEmailForm():	
	print('<form method = post action = "changeEmail.py">')
	print('<fieldset><legend>Change your email address</legend>')
	print('Current Email Address: <input type = text name = "oldEmail" required><br>')
	print('New Email Address: <input type = text name = "newEmail" required><br>')
	print('<input type=submit value="Submit">')
	print('</fieldset></form><br>')
	    
main()