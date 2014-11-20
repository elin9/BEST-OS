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

def main():
    aCookie = Cookie.SimpleCookie(cookie_string)
    userCookie = aCookie['name'].value
    userForm = form.getvalue("user")
    titleForm = form.getvalue("title") 
     
    if userCookie == userForm:
    	c.execute('delete from bookposts where user = ? and title = ?', (userCookie, titleForm,))
   	conn.commit()
    	conn.close()   
    	
    print("Content-type: text/html")
    print("")
    print("<html><head><title>Delete Post</title></head><body>") 
    print(titleForm + " has been successfully deleted<br>")
    print('Return to <a href="http://test.elin9.rochestercs.org/cgi-bin/editSettings.py">settings</a>.')
    print("</body></html>")

main()