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
		# following code block is from jqueryui.com/tabs
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
		
		#print '<script type="text/javascript">'
		#print '$(document).ready(function() {'
		#print 'console.log("Loaded!");'
		#print '$("#tabs-1").load("printUserPost.py");'
		#print 'if ($.cookie("name") != undefined) {'
		#print '$("#right").append("Hi, " + $.cookie("name") + "!<br>");'
		#print '$("#right").append("You are logged in.<br>");}'         
		#print '});'
		#print '</script>'
		
		print '<script type="text/javascript">'
		print """
		$(document).ready(function() {
			var list="";
			console.log("Loaded!");
			if ($.cookie("name") != undefined) {
				$("#right").append("Hi, " + $.cookie("name") + "!<br>");
				$("#right").append("You are logged in.<br>");}
			
			$("#tabs-1-posts").load("printUserPost.py", function(){
				$(this).find($('.check')).each(function(){
					$(this).click(function(){
						if($(this).is(':checked')){
							list+=$(this).val()+" | ";
						}else{
							if (list.toLowerCase().indexOf($(this).val()+"&") >= 0){
								list=list.replace($(this).val()+" & ", '');
							}
						}
					});
				});
			});
		
			$('#dle').click(function(){
				user = $('input[name="sid"]').val();
				$.post('/cgi-bin/deletePost.py', {list: list, user: user}, function(data){
					alert("You are about to delete: "+ list);
					console.log("success "+data);
					$("#tabs-1").load("printUserPost.py");
				});
 			});
 		});"""
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
		print """<div id="tabs">
			  <ul>
			    <li><a href="#tabs-1">Your Textbooks</a></li>
			    <li><a href="#tabs-2">Change Contact Info</a></li>
			    <li><a href="#tabs-3">Delete Your Account</a></li>
			  </ul>
			  <div id="tabs-1">
			  	<button id="dle">Delete</button>
	       			<input id="selectAll" type="checkbox" value="SelectAll">SelectAll
	       			<div id="tabs-1-posts"></div>
			  </div>
			  <div id="tabs-2">"""
		changeEmailForm()
		print " </div>"
		print "	  <div id=\"tabs-3\">"
		deleteAccountForm()
		print """ </div>
			</div>
			</body></html>"""		
	else:
		print "Content-type: text/html"
		print
		print "<html><head><title>Settings</title></head><body>"
		print 'Please return to <a href = "http://test.elin9.rochestercs.org/cgi-bin/index.php">home</a> and login.'		
		print "</body></html>"
	
def changeEmailForm():	
	print('<form method = post action = "changeEmail.py">')
	print('<fieldset><legend>Change your email address</legend>')
	print('Current Email Address: <input type = text name = "oldEmail" required><br>')
	print('New Email Address: <input type = text name = "newEmail" required><br>')
	print('<input type=submit value="Submit">')
	print('</fieldset></form><br>')
    
def deleteAccountForm():
	print('<form method = post action = "deleteUsertry.py">')
	print('<fieldset><legend>To delete your account, enter your username and password</legend>')
	print('Username <input type = text name = "username" required><br>')
	print('Password <input type = password name = "password" required><br>')
	print('<input type=submit value="Submit">')
	print('</fieldset></form><br>')

main()