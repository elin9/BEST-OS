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
c = conn.cursor()

def main():
	user = "Test" #get username of the user who is logged in from the database...
	title = form.getvalue("title")
	author = form.getvalue("author")
	edition = form.getvalue("edition")
	isbn = form.getvalue("isbn")
	condition = form.getvalue("condition")
	otherNotes = form.getvalue("othernotes")
	courseNum = form.getvalue("courseNum")
	photo = form.getvalue("photo")
	price = form.getvalue("price")

	"""c.execute('UPDATE bookposts SET
			user=?,
			title=?,
			author=?,
			edition=?
			ISBN=?,
			condition=?,
			otherNotes=?,
			courseNumber=?,
			photo=?,
			price=?',
		    	(user, title, author, edition, isbn, condition, otherNotes, courseNum, photo, price))
	conn.commit()"""
	
	print "Content-type: text/plain"
	print
	print form
	print user
	print title
	print author
	print edition
	print isbn
	print condition
	print otherNotes
	print courseNum
	print photo
	print price
	
main()