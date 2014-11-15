#!/usr/bin/python

import cgitb
import sqlite3
import os 
import Cookie
cgitb.enable()

cookie_string = os.environ.get('HTTP_COOKIE')
conn = sqlite3.connect('BESTOS_DATABASE.db')
c = conn.cursor()

aCookie = Cookie.SimpleCookie(cookie_string)
usr = aCookie['name'].value
print "Content-type: text/html"
print 
    
for row in c.execute('select * from bookposts where user=? order by datePosted desc;',(usr,)):	
	print '<div class = "post" style = "border: 1px solid #000000; height: 200px;">'
	print '<p class="leftcontent" style="float:left; width:70px; padding-left:0.3em;">'
	print '<br>Course: %s' %row[11]
	print '  %s' %row[7]
	print '<p class="photo" style="float:left; width:100px; position:relative; padding-left:0.3em;">'
	print '<img id="try" style = "width: 120px; height: 160px; float: left; border: 1px solid #000;" src = "%s">' %row[8]
	print '<p class="rightcontent" style="float:left; position:relative; left:10%; width:350px;">'
	print '<br>Title: %s' %row[1]
	print '<br>Author: %s' %row[2]		
	print '<br>Edition: %s' %row[3]
	print '<br>ISBN: %s' %row[4]
	print '<br><br>Condition: %s' %row[5]
	print '<br>Other Notes: %s' %row[6]
	print '<div class="rightcontent2" style="float:left; position:relative; right=20%; text-align:end;">'
	print '<p id="price" style="font-size:30pt;">$%s</p>' %row[9]
	print '<form id = "delete" action = "deletePost.py"><input type = hidden name = "user" value = %s>' %row[0]
	print '<input type = hidden name = "title" value = %s>' %row[1]
	print '<br> <input type=submit value = "Delete Post"></form>'
	print '</div></p></div><br><br>'
conn.close()
