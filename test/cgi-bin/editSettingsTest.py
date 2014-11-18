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
	if cookie_string:
		aCookie = Cookie.SimpleCookie(cookie_string)
		user = aCookie['name'].value
		print "Content-type: text/html"
		print 
		print "<html><head><title>Settings</title>"
		print """<head>
			  <meta charset="utf-8">
			  <link rel="stylesheet" href="//code.jquery.com/ui/1.11.2/themes/smoothness/jquery-ui.css">
			  <script src="//code.jquery.com/jquery-1.10.2.js"></script>
			  <script src="//code.jquery.com/ui/1.11.2/jquery-ui.js"></script>
			  <script src=\"http://elin9.rochestercs.org/jquery.cookie.js\"></script>
			  <link rel="stylesheet" href="/resources/demos/style.css">
			  <script>
			  $(function() {
			    $( "#tabs" ).tabs();
			  });
			  </script>
			</head>"""
		#print "<link rel = \"stylesheet\" type = \"text/css\" href=\"http://elin9.rochestercs.org/experimenting/style.css\">"
		
		print '<script type="text/javascript">'
		print '$(document).ready(function() {'
		print 'console.log("Loaded!");'
		print '$("#tabs-1").load("printUserPost.py");'
		print 'if ($.cookie("name") != undefined) {'
		print '$("#right").append("Hi, " + $.cookie("name") + "!<br>");'
		print '$("#right").append("You are logged in.<br>");}'         
		print '});'
		print '</script>'
		
		print '<body>'
		print '<div id="header"><div id ="banner" style = "z-index:1;">'
		print '<a href = "http://test.elin9.rochestercs.org/cgi-bin/index.php"><img src="http://elin9.rochestercs.org/img/banner2.png"/></a></div>'
		print '<div id = "loginbox">'
		print "<form style = \"display: inline;\"method = post action = \"http://test.elin9.rochestercs.org/cgi-bin/logout.py\">"
		print "<input type = hidden name = \"sid\" value = " + str(user) + ">"
		print "<input type=submit name = \"logout\" value = \"Logout\"></form>"
		print "</div></div>"
		print '<div id="right" class="column"></div>'
		
		# following code block from jqueryui.com/tabs/
		print """<div id="tabs">
			  <ul>
			    <li><a href="#tabs-1">Your Textbooks</a></li>
			    <li><a href="#tabs-2">Change Contact Info</a></li>
			    <li><a href="#tabs-3">Delete Your Account</a></li>
			  </ul>
			  <div id="tabs-1">
			    <p>...List user's textbooks here...</p>
			  </div>
			  <div id="tabs-2">
			    <p>...Put change email address form here...</p>
			  </div>
			  <div id="tabs-3">
			  	<p>...Change so that the form appears here...</p>
				<form style = \"display: inline;\" method = post action = \"http://test.elin9.rochestercs.org/cgi-bin/deleteUser.py\">
				<input type=submit name = \"delete\" value = \"Delete your account\"></form>
			  </div>
			</div>"""
		print '</body></html>'		
	else:
		print "Content-type: text/html"
		print
		print "<html><head><title>Settings</title></head><body>"
		print 'Please return to <a href = "http://test.elin9.rochestercs.org/cgi-bin/index.php">home</a> and login.'		
		print "</body></html>"
			

main()