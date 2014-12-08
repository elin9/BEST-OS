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
		oldPass = form.getvalue("oldPass")
		newPass = form.getvalue("newPass")
		c.execute('select password from users where username = ?',(user,))
	   	dbPass = str("%s" % c.fetchone())

		print "Content-type: text/html"
		print
		print "<html><head><title>Change Email</title></head><body>"
		if oldPass != dbPass:
			print "The current password you entered does not match.<br>"
			changePasswordForm()
		else:
			c.execute('update users set password = ? where username = ?;', (newPass, user))
			conn.commit()
			print "You have successfully changed your password.<br>"
			print "Return to <a href='http://elin9.rochestercs.org/cgi-bin/editSettingsTabs.py'>settings</a>."
		conn.close()
		print "</body></html>"

def changePasswordForm():	
	print('<form id="changePasswordForm" method = post action = "changePassword.py">')
	print('<fieldset><legend>Change your password</legend>')
	print('Current Password Address: <input type = password name = "oldPass" required><br>')
	print('New Password: <input type = password name = "newPass" required><br>')
	print('<input type=submit value="Submit">')
	print('</fieldset></form><br>')
	    
main()