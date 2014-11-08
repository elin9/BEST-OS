<!DOCTYPE html>

<html>
<head>
<title>Home</title>
<link rel = "stylesheet" type = "text/css" href="http://elin9.rochestercs.org/experimenting/style.css">
<script src="http://elin9.rochestercs.org/jquery-1.11.0.js"></script>
<script src="http://elin9.rochestercs.org/menu.js"></script>
<script src="http://malsup.github.com/jquery.form.js"></script> 
<script src="http://elin9.rochestercs.org/jquery.cookie.js"></script>

<script type="text/javascript">

$(document).ready(function() {
  console.log("Loaded!");
  $("#bookpost").load("printTextbook.py");
  
  $('#json-one').change(function(){
	console.log("the user has selected a school");
	//$('#json-two').attr('size', 20);
	//$('#json-two').css("width", "254px");
  });
  
  $('#form-json-one').change(function(){
	console.log("school selected in bookposts form");
  });
  
  if ($.cookie("name") != undefined) {
	$("#right").append("Hi, " + $.cookie("name") + "!<br>");
	$("#right").append("You are logged in.<br>");
	$('#postABook').css('display','block')
				   .click(function(){
						$('#postform').toggle();
					});
  }
          
  $('#postsomething').ajaxForm(function() { 
  
      var user = $.cookie("name");
      var title = $('#postsomething').find('input[name="title"]').val();
      var author = $('#postsomething').find('input[name="author"]').val();
      var edition = $('#postsomething').find('input[name="edition"]').val();
      var isbn = $('#postsomething').find('input[name="isbn"]').val();
      var condition = $('#postsomething').find('select[name="condition"]').val();
      var otherNotes = $('#postsomething').find('input[name="othernotes"]').val();
      var school = $('#postsomething').find('select[name="school"]').val();
      var course =$('#postsomething').find('select[name="course"]').val();
      var courseNum = $('#postsomething').find('input[name="courseNum"]').val();
      var photo = $('#postsomething').find('input[name="photo"]').val();
      var price = $('#postsomething').find('input[name="price"]').val();
  		
      console.log(course);
      $.ajax(
      {
        url: "http://elin9.rochestercs.org/cgi-bin/postTextbook.py",
        type: "POST",
        dataType: "text",
        data: {user: user, title: title, author: author, edition: edition, isbn: isbn, condition: condition, othernotes: otherNotes, school: school, course: course, courseNum: courseNum, photo: photo, price: price},

        success: function(data) {
          console.dir(data);
          $("#bookpost").prepend("Seller: " + user+ " | Title: " + title + " | Author: " + author + " | Edition: " + edition + " | ISBN: " + isbn + " | Condition: " + condition + " | Other Notes: " + otherNotes + " | Course Number: " + courseNum + " | Photo: " + photo + " | Price: $" + price + " | School: " + school + " | Course: " + course + "<br><br>");
          console.log("book posted!");
          //window.location.replace('http://elin9.rochestercs.org/cgi-bin/index.php');
        },
      }
    );
  });

  $('#login').ajaxForm(function() { 
      var un = $('#login').find('input[name="username"]').val();
      var ps = $('#login').find('input[name="password"]').val();
      $.ajax(
      {
        url: "http://elin9.rochestercs.org/cgi-bin/login2.py",
        type: "POST",
        dataType: "text",
        data: {username: un, password: ps,},

        success: function(data) {
          console.dir(data);
          $("#right").append("You are now logged in.<br>");
          window.location.replace('http://elin9.rochestercs.org/cgi-bin/index.php');
          if ($.cookie("name") === undefined){
             $("#right").append(data + "<br>");
          } else{
             console.log("logged in!");
             $("#right").append("Hi, " + data + "!<br>");
             window.location.replace('http://elin9.rochestercs.org/cgi-bin/index.php');
          }
        },
      }
    );
  });

});

function load()
{
  $.ajax({
      type:"POST",
      url: "http://elin9.rochestercs.org/cgi-bin/printTextbook.py",
      data: {school: $("#json-one").val(), course: $("#json-two").val()},
      success: function(data) {
          console.dir(data);
          $("#bookpost").html(data);
      }
  });
}
 
</script>
</head>
<body>
	<div id="header">
		<div id ="banner">
			<a href = "http://elin9.rochestercs.org/cgi-bin/index.php"><img src="http://elin9.rochestercs.org/img/banner.png"/></a>
		</div>
	 	<div id = "loginbox">
		 	<?php
			$cookie_name = "sessionID";
			if(!isset($_COOKIE[$cookie_name])) {
			    echo "<form id = \"login\" method = post action = \"login2.py\">";
			    echo "Username:<input name=\"username\" type=text size=\"20\" required/> ";
			    echo "Password:<input name=\"password\" type=password size=\"20\" required/>";
			    echo "<input type = submit name = \"submit\" value = \"Login\"/></form><br>";
			} else {
			    echo "<form style = \"display: inline;\" method = post action = \"http://elin9.rochestercs.org/cgi-bin/deleteUser.py\">";
			    echo "<input type=submit name = \"delete\" value = \"Delete your account\"></form> ";
			    echo "<form style = \"display: inline;\"method = post action = \"http://elin9.rochestercs.org/cgi-bin/logout.py\"> ";
			    echo "<input type = hidden name = \"sid\" value = " . $_COOKIE[$cookie_name] . ">";
			    echo "<input type=submit name = \"logout\" value = \"Logout\"></form>";
			}
			?>
		</div>
	 </div>
        <div id="container">
            <div id="center" class="column" style="left: 80px;">Textbooks For Sale<br>
            	<input type="button" value="SELL A TEXTBOOK" id="postABook" style="display:none;">
            	<div id="postform" style="width: 700px; display: none;"><br>
            	<?php
		$cookie_name = "sessionID";
		if(isset($_COOKIE[$cookie_name])) {
		    	echo "<form id = \"postsomething\" method = post>";
	            	
	            	echo "<fieldset>";
	            	echo "<legend>Enter in the following information about the textbook you want to sell:</legend>";
	            	echo "<label for= \"Title\">Title:</label><input name = \"title\" class=\"try\" type = text required/>";
	            	echo "<label for= \"Author\">Author:</label><input name = \"author\" class=\"try\" type = text required/><br>";
	            	echo "<label for= \"Edition\">Edition:</label><input name = \"edition\" class=\"try\" type = text required/>";
	            	echo "<label for= \"ISBN\">ISBN:</label><input name = \"isbn\" class=\"try\" type = text required/><br>";
			echo '<label for= "Condition">Condition:</label>
				<select name="condition" class="try" id="cond">
					<br><pre><option selected value="base">Select a condition</option></pre>
					<option value="Poor">Poor</option>
					<option value="Fair">Fair</option>
					<option value="Good">Good</option>
					<option value="Very Good">Very Good</option>
					<option value="Like New">Like New</option>
					<option value="Brand New">Brand New</option>
				</select><br>';
	            	echo '<label for= "School">School:</label><select name = "school" class="try" id="form-json-one">
					<br><pre><option selected value="base">Select a school</option></pre>
					<option value="ASE">Arts Sciences and Engineering</option>
					<option value="Simon">Simon School of Business Administration</option>
					<option value="Warner">Warner School of Education</option>
					<option value="Eastman">Eastman School of Music</option>
					<option value="Medicine">School of Medicine and Dentistry</option>
				      </select><br>';
			        echo '<label for= "Course">Course:</label><select name="course" class="try" id="form-json-two" >
					<option>Select a school above</option>
				      </select><br>';
// 			echo "Course: <input name = \"course\" type = text required/><br>";
	            	echo "<label for= \"CourseNumber\">Course Number (e.g. 210):</label><input name = \"courseNum\" class=\"try\" type = number min = \"0\" required/><br>";
	            	echo "<label for= \"Photo\">Photo (link to a photo):</label><input name = \"photo\" class=\"try\" type = text required/><br>";
	            	echo "<label for= \"Price\">Price (enter number):</label><input name = \"price\" class=\"try\" type = number step = \"0.01\" min = \"0\" required/><br>";
	            	echo "<label for= \"Other notes\">Other notes:</label><input name = \"othernotes\" class=\"try\" type = text /><br>";
	            	echo "<input name = \"submit\" type = submit value = \"Sell a Textbook!\"/>";
	            	echo "</fieldset>";
	            	
	            	echo "</form><br><br>";
		}
		?>
	            </div>
	        <div id = "searchpost" style="width: 700px;">
            	    <div id = "bookpost" style="width: 700px;"></div>
            	</div>
            </div>
            <div id="left" class="column">
            	<label for= "class" accesskey="c">Class</label>
				<select id="json-one">
					<br><pre><option selected value="base">Please Select a school</option></pre>
					<option value="ASE">Arts Sciences and Engineering</option>
					<option value="Simon">Simon School of Business Administration</option>
					<option value="Warner">Warner School of Education</option>
					<option value="Eastman">Eastman School of Music</option>
					<option value="Medicine">School of Medicine and Dentistry</option>
				</select>
	
				<br/>
				<form method="post" action="cgi-bin/search.php">
				<select name="courseNum" id="json-two" >
					<option>Please choose from above</option>
				</select>
				<input type="button" value="Search" onClick="load()"></input>
				</form>
				
			 </div>
             <div id="right" class="column">
           	<?php
		$cookie_name = "sessionID";
		if(!isset($_COOKIE[$cookie_name])) {
           		echo "Or <a href = \"http://elin9.rochestercs.org/cgi-bin/form.py\">Create an Account</a>";
           	}?>
             </div>
    	</div>
        <div id="footer-wrapper">
              <div id="footer"></div>
        </div>
  
</body>
</html>