#!/usr/bin/python

import cgi
import cgitb
cgitb.enable()
import sqlite3

form = cgi.FieldStorage()

def main():
    print("Content-type: text/html")
    print("")
    conn = sqlite3.connect('BESTOS_DATABASE.db')
    c = conn.cursor()
    school = form.getvalue("school")
    course = form.getvalue("course")
    schoolFilter = None
    courseFilter = None

# 	getrow(0,c)
    if str(school)== "None" or str(school) == "base":
#     	    print '<div class = "post" style = "border: 1px solid #000000; height: 200px;">\
#     	    <p class="post" >Seller: %s | Title: %s | Author: %s | Edition: %s | ISBN: %s | Condition: %s | \
#     	    Other Notes: %s | Course Number: %s | \
#     	    <img style = "width: 50px; height: 70px; float: left;" src = "%s"> \
#     	    Price: $%s | School: %s | Course: %s | Date Posted: %s GMT <p></div>' % row
#     	    print("<br><br>")
		for row in c.execute('select * from usersNbooks order by datePosted desc'):	
			print '<div class = "post" style = "border: 1px solid #000000; height: 200px;">'
			print '<p class="leftcontent" style="float:left; width:70px; padding-left:0.3em;">'
			print '<br>Course: %s' %row[11]
			print '  %s' %row[7]
			print '<p class="photo" style="float:left; width:100px; position:relative; padding-left:0.3em;">'
			print '<img id="try" style = "width: 120px; height: 160px; float: left; border: 1px solid #000;" src = "%s">' %row[8]
			print '<p class="rightcontent" style="float:left; position:relative; left:10%; width:350px; word-wrap:break-word;">'
			print '<br>Title: %s' %row[1]
			print '<br>Author: %s' %row[2]
			print '<br>Edition: %s' %row[3]
			print '<br>ISBN: %s' %row[4]
			print '<br><br>Condition: %s' %row[5]
			print '<br>Other Notes: %s' %row[6]
			print '<div class="rightcontent2" style="float:left; position:relative; right=20%; text-align:end;">'
			print '<p id="lalala" style="font-size:30pt;">$%s</p>' %row[9]
			#print '<br> <button id="contact" >Contact %s</button>' %row[0]
			print '<br> Email %s at:' %row[0]
			print '<br>%s'  %row[13]
			print '</div>'
			print '</p></div><br><br>'
    else:
        print "Showing textbooks for " + str(school) + " " + str(course) + ":<br><br>"
    	for row in c.execute('select * from bookposts where school = ? and course = ? collate nocase order by datePosted desc;',(str(school),str(course))):
    	    print '<div class = "post" style = "border: 1px solid #000000; height: 200px;">Seller: %s | Title: %s | Author: %s | Edition: %s | ISBN: %s | Condition: %s | Other Notes: %s | Course Number: %s | <img style = "width: 50px; height: 70px; float: left;" src = "%s"> Price: $%s | School: %s | Course: %s | Date Posted: %s GMT </div>' % row
    	    print("<br><br>")
    conn.close()

def checkNone(num):
		if num is None:
			num="none"
		else:
			return num
			

main()