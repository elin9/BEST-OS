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
		oldEmail = form.getValue("oldEmail")
		newEmail = form.getValue("newEmail")
		#c.execute('select email from users where username = ?',(user,))
	   	#dbEmail = str("%s" % c.fetchone())
	    	#print dbEmail
	    	#c.execute('select username from users where email = ?',(newEmail,))
	    	#emailInDB = str("%s" % c.fetchone())

		print "Content-type: text/html"
		print
		#if oldEmail != dbEmail:
		#	print "The current email address you entered does not exist.<br>"
		#	changeEmailForm()
		#	elif str(emindb) != "None":
		#    		print "An account already exists with this email.<br>"
		#    		changeEmailForm()
		#    	else:
		#		c.execute('update users set email = ? where username = ? and email = ?;', (newEmail, user, oldEmail))
		#		conn.commit()
		#		print "You have changed your email address to " + str(newEmail) + "<br>"
		#conn.close()

def changeEmailForm():	
	print("""<form method = post action="changeEmail.py"><fieldset><legend>Change your email address</legend>
	    Current Email Address: <input type = text name = "oldEmail" required><br>
	    New Email Address: <input type = text name = "newEmail" required><br>
	    <input type=submit value="Submit">
	    </fieldset></form><br>""")
	    
main()