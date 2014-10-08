#!/usr/bin/python
import cgi, Cookie, os, sqlite3
import cgitb
cgitb.enable()

conn=sqlite3.connect('BESTOS_DATABASE.db')
c=conn.cursor()

cookie_string=os.environ.get('HTTP_COOKIE')
if cookie_string:
	my_cookie=Cookie.SImpleCookie(cookie_string)
	saved_session_id=my_cookie['session_id'].value
	
	c.execute('select * from users where sessionID=?',(saved_session_id,))
	all_results=c.fetchall()
	if len(all_results)>0:
		saved_name = all_results[0][0]
		print "Content-type: text/html"
		print 
		print "<html>"
		print "<body>"
		print "<h1>welcome back "+ saved_name + "</h1>"
		print "</body>"
		print "</html>"
	else:
		print "Content-type: text/html"
                print
                print "<html>"
                print "<body>"
                print "<h1>you are not registered</h1>"
                print "</body>"
                print "</html>"
