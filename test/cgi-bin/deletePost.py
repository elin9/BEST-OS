#!/usr/bin/python

import cgi
import cgitb
import sqlite3
import os
import Cookie
import json
cgitb.enable()

form = cgi.FieldStorage()
cookie_string = os.environ.get('HTTP_COOKIE')

conn = sqlite3.connect('BESTOS_DATABASE.db')
c = conn.cursor()
aCookie = Cookie.SimpleCookie(cookie_string)
userCookie = aCookie['name'].value
userForm = form.getvalue("user")
titleForm = form.getvalue("list") 
    
def main():
    titles=titleForm.split(", ")
    for t in titles[:]:
    	c.execute('select photo from bookposts where user = ? and title = ?', (userCookie,t,))
    	p = str("%s" %c.fetchone())
    	c.execute('delete from bookposts where user = ? and title = ?', (userCookie,t,))
    	titles.remove(t)
   	conn.commit()
    conn.close()   
#     	
    print("Content-type: text/html")
    print
    
    print("<html><head><title>Delete Post</title></head><body>") 
#     print "this is %s" % p
    print("Successfully deleted post<br>")
    print('Return to <a href="http://test.elin9.rochestercs.org/cgi-bin/editSettings.py">settings</a>.')
    print("</body></html>")

main()