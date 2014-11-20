#!/usr/bin/python

import cgi
import datetime
import cgitb
import os
import Cookie
import sqlite3
cgitb.enable()

form = cgi.FieldStorage()
title = form.getvalue('title')
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
		print "<link rel = \"stylesheet\" type = \"text/css\" href=\"http://elin9.rochestercs.org/experimenting/style.css\">"
		print "<script src=\"http://elin9.rochestercs.org/jquery-1.11.0.js\"></script>"
		print "<script src=\"http://malsup.github.com/jquery.form.js\"></script>"
		print "<script src=\"http://elin9.rochestercs.org/jquery.cookie.js\"></script>"
		print '<script type="text/javascript">'
		print """
		$(document).ready(function() {
			var list="";
			console.log("Loaded!");
			if ($.cookie("name") != undefined) {
			$("#right").append("Hi, " + $.cookie("name") + "!<br>");
			$("#right").append("You are logged in.<br>");}
			
			$("#bookpost").load("printUserPost.py", function(){
				$(this).find($('.check')).each(function(){
					$(this).click(function(){
						if($(this).is(':checked')){
							list+=$(this).val()+", ";
						}else{
							if (list.toLowerCase().indexOf($(this).val()+", ") >= 0){
								list=list.replace($(this).val()+", ", '');
							}
						}
					});
				});
			});
		
			$('#dle').click(function(){
				user = $('input[name="sid"]').val();
				$.post('/cgi-bin/deletePost.py', {list: list, user: user}, function(data){
					alert("You are about to delete this: "+ list);
					console.log("success"+data);
					$("#bookpost").load("printUserPost.py");
				});
 			});
 		});"""
		print '</script>'
		print '</head>'

		print '<body>'
		print '<div id="header"><div id ="banner" style = "z-index:1;">'
		print '<a href = "http://test.elin9.rochestercs.org/cgi-bin/index.php"><img src="http://elin9.rochestercs.org/img/banner2.png"/></a></div>'
	 	print '<div id = "loginbox">'
		print '<form style = "display: inline;" method = post action = "/cgi-bin/deleteUser.py">'
		print '<input type=submit name = "delete" value = "Delete your account"></form>'
		print "<form style = \"display: inline;\"method = post action = \"/cgi-bin/logout.py\">"
		print "<input type = hidden name = \"sid\" value = " + str(user) + ">"
		print "<input type=submit name = \"logout\" value = \"Logout\"></form>"
		print "</div></div>"
		print '<div id="container">'
	        print '<div id="center" class="column" style="left:-60px;">'
	        print '<br><button id="dle">Delete</button>'
	        print '<input id="selectAll" type="checkbox" value="SelectAll">SelectAll'
		print '<br><div id = "bookpost" style="width: 750px;"></div>'
	        print '</div>'
	        print '<div id="left" class="column">Your Textbooks<br>'
	        print '</div>'
		print '<div id="right" class="column"></div>'
		print '</div>'
		print '<div id="footer-wrapper"><div id="footer"></div></div>'
		print '</body></html>'
	else:
		print "Content-type: text/html"
		print
		print "<html><head><title>Settings</title></head><body>"
		print 'Please return to <a href = "/cgi-bin/index.php">home</a> and login.'
		print "</body></html>"


main()