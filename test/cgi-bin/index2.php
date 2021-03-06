<!DOCTYPE html>

<html>
<head>
<title>Home</title>
<link rel = "stylesheet" type = "text/css" href="http://elin9.rochestercs.org/experimenting/style2.css">
<script src="http://elin9.rochestercs.org/jquery-1.11.0.js"></script>
<!-- <script src='http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.5/jquery-ui.min.js'></scr‌ipt> -->
<script src="http://test.elin9.rochestercs.org/menu.js"></script>
<script src="http://malsup.github.com/jquery.form.js"></script> 
<script src="http://elin9.rochestercs.org/jquery.cookie.js"></script>
<script src="http://test.elin9.rochestercs.org/jpaginate.js" type="text/javascript"></script>

<script type="text/javascript">
var photo;
$(document).ready(function() {
  console.log("Loaded!");
  $('#bookpost').load('printTextbook.py',function(){
    			// var i = 1;
    			var showperpage = 5; 
    			var post = $(this).find($('.post'));
				var totalContent = post.length;

				$(this).find($('.post')).slice(showperpage).hide();
				
				$('#pages').pagination({
        			items: totalContent,
        			itemsOnPage: showperpage,
        			cssStyle: 'light-theme',
        			onPageClick: function(pageNumber) { // this is where the magic happens
            			// someone changed page, lets hide/show trs appropriately
//             			alert('click page '+pageNumber+' and showing '+showperpage+' contents');
            			var showFrom = showperpage * (pageNumber - 1);
            			var showTo = showFrom + showperpage;
// 						alert('show from content '+showFrom+' to content '+showTo);
           				post.hide()
           				    .slice(showFrom, showTo).show();
        			}
    			});
    		});
  
  $('#json-one').change(function(){
	console.log("the user has selected a school");
	//$('#json-two').attr('size', 20);
	//$('#json-two').css("width", "254px");
  });
  
  $('input[type="text"]').keyup(function(){
  	$('input[name="reset"]').attr('disabled',false);
  	$('input[name="reset"]').click(function(){
		$('#form-json-two').val('Please choose from above');
		if($('#previewPic').is( ":hidden" )){
		}else{
			$('#preview').replaceWith('<div id="preview">'+'</div>');
			$('#previewPic').toggle();
		}
  	});
  });
  
  // $('#loginbox').mouseenter(function(){
// 	if($('#login').length){
// 		$(this).css({
// 			'bottom':'380px',
// 			'position':'fixed'
// 
//     	});
// 	}
// 	else{
// 		$(this).css({
// 			'bottom':'458px',
// 			'position':'fixed'
// 
//     	});
// 	}
// 	
//     
//   });
// 
//   $('#loginbox').mouseleave(function(){
// 	
// 	$(this).css({
// 		'bottom':'458px',
// 		'position':'fixed'
//     });
// 
//   });
  		
//   	
 
  
  $('#form-json-one').change(function(){
	console.log("school selected in bookposts form");
  });
  
  //----------------------------
  $('#pic').change(function(){
    $('#previewPic').toggle();
    $('#preview').replaceWith('<br>'+'<br>'+'<div id="preview">'+'</div>');
  	readURL(this); //preview the pic and get the url
  });
  
  $('#upload').click(function(){
  		console.log("happy upload");
  		var file = $('#previewPic').attr('src');
  		var title = $('#postsomething').find('input[name="title"]').val();
  		var user = $.cookie("name");
//   		var file =file.split('base64,')[1];
//   		console.log(file);
		var fd = new FormData();
    	fd.append("file",file);
		$.ajax(
		{
        	url: "http://test.elin9.rochestercs.org/upload.php",
        	type: "POST",
			contentType: false,
			processData: false,
        	data: fd,

        	success: function(data) {
        		console.log(data);
				photo = 'http://test.elin9.rochestercs.org/'+data;
        	}, 
  		});
	});
	
	$('#remove').click(function(){
  		console.log("happy remove "+photo);
		$.post('http://test.elin9.rochestercs.org/remove.php',{photo: photo})
		.done(function(data){
			if($('#previewPic').is( ":hidden" )){
		}else{
			$('#preview').replaceWith('<div id="preview">'+'</div>');
			$('#previewPic').toggle();
			$('#pic').replaceWith($('#pic').val('').clone(true));
		}
		});

	});

//----------------------------
  
  if ($.cookie("name") != undefined) {
	$("#right").append("Hi, " + $.cookie("name") + "!<br>");
	$("#right").append("You are logged in.<br>");
	$('#postABook').css('display','block')
				   .click(function(){
						$('#postform').toggle();
					});
  }
        
  $('#postsomething').ajaxForm(function() { 
  	  console.log(photo);
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
      
      var price = $('#postsomething').find('input[name="price"]').val();
  		
      console.log(course);
      $.ajax(
      {
        url: "http://test.elin9.rochestercs.org/cgi-bin/postTextbook.py",
        type: "POST",
        dataType: "text",
        data: {user: user, title: title, author: author, edition: edition, isbn: isbn, condition: condition, othernotes: otherNotes, school: school, course: course, courseNum: courseNum, photo: photo, price: price},

        success: function(data) {
          console.dir(data);
          $("#bookpost").load("printTextbook.py");
          //$("#bookpost").prepend("<div class = \"post\" style = \"border: 1px solid #000000; height: 100px;\">Seller: " + user+ " | Title: " + title + " | Author: " + author + " | Edition: " + edition + " | ISBN: " + isbn + " | Condition: " + condition + " | Other Notes: " + otherNotes + " | Course Number: " + courseNum + "<img style = \"width: 50px; height: 70px; float: left;\" src = \""+photo+"\"> | Price: $" + price + " | School: " + school + " | Course: " + course + "</div><br><br>");
          console.log("book posted!");
          //window.location.replace('http://test.elin9.rochestercs.org/cgi-bin/index.php');
        },
      }
    );
  });

  $('#login').ajaxForm(function() { 
      var un = $('#login').find('input[name="username"]').val();
      var ps = $('#login').find('input[name="password"]').val();
      $.ajax(
      {
        url: "http://test.elin9.rochestercs.org/cgi-bin/login2.py",
        type: "POST",
        dataType: "text",
        data: {username: un, password: ps,},

        success: function(data) {
          console.dir(data);
          //window.location.replace('http://test.elin9.rochestercs.org/cgi-bin/index.php');
          if ($.cookie("name") === undefined){
             $("#right").append(data + "<br>");
          } else{
             console.log("logged in!");
             $("#right").append("Hi, " + data + "!<br>");
             $("#right").append("You are now logged in.<br>");
             window.location.replace('http://test.elin9.rochestercs.org/cgi-bin/index.php');
          }
        },
      }
    );
  });

});

// function pop(){
// 	    $('#show').load('form.py',function(){
// 	    	$(this).find('a').css({'color':'#123456', 'font-weight':'bold'})
// 	    	.click(function(){
// 	    		$(this).attr('href','#');
// 	    		$('#show').hide();
// 	    		$('#overlay').remove();
// 	    	});
// 	    	$(this).find('input[type="submit"]').click(function(){
// 	    		 $('#show').load('form.py');
// 	    	});
// 	    }).show();
// 		$('body').append('<div class="overlay" id="overlay"></div>');
// 		
// 		// $('#close').click(function(){
// // 			$('#show').hide();
// // 			$('#overlay').remove();
// // 		});
// }
function load()
{
  var school = $("#json-one").val();
  var course = $("#json-two").val();
  var searchString = school + " " + course;
  $("#showing").html("Showing textbooks for " + searchString + ":<br><br>");
  $("div.post:not(:contains('"+searchString+"'))").hide();
  $("div.post:contains('"+searchString+"')").show();
  
}

function submitForm()
{
    document.forms["bookpostform"].submit();
    document.forms["bookpostform"].reset();
}
 
//----------------------------
function readURL(input){
	if(input.files && input.files[0]){
		var reader = new FileReader();
		reader.onload = function (e){
			$('#previewPic').attr('src', e.target.result);
			// console.log($('#previewPic').attr('src'));
		};	
		reader.readAsDataURL(input.files[0]);
	} //if the file is uploaded
}



</script>
</head>
<body>
<!-- -facebook -->
	<script>
  window.fbAsyncInit = function() {
    FB.init({
      appId      : '1529004984024188',
      xfbml      : true,
      version    : 'v2.2'
    });
  };

  (function(d, s, id){
     var js, fjs = d.getElementsByTagName(s)[0];
     if (d.getElementById(id)) {return;}
     js = d.createElement(s); js.id = id;
     js.src = "//connect.facebook.net/en_US/sdk.js";
     fjs.parentNode.insertBefore(js, fjs);
   }(document, 'script', 'facebook-jssdk'));
	</script>
<!-- -facebook -->
	<div id="header">
		<div id ="banner" style = "z-index:1;">
			<a href = "http://test.elin9.rochestercs.org/cgi-bin/index.php"><img src="http://elin9.rochestercs.org/img/bann.png"/></a>
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
			    //echo "<form style = \"display: inline;\" method = post action = \"http://test.elin9.rochestercs.org/cgi-bin/deleteUser.py\">";
			    //echo "<input type=submit name = \"delete\" value = \"Delete your account\"></form> ";
			    echo "<form style = \"display: inline;\" method = post action = \"http://test.elin9.rochestercs.org/cgi-bin/editSettingsTabs.py\">";
			    echo "<input type=submit name = \"usersettings\" value = \"Account Settings\"></form> ";
			    echo "<form style = \"display: inline;\"method = post action = \"http://test.elin9.rochestercs.org/cgi-bin/logout.py\"> ";
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
		    	echo "<form id = \"postsomething\" name = \"bookpostform\" method = post >";
	            	
	            	echo "<fieldset>";
	            	echo "<legend>Enter in the following information about the textbook you want to sell:</legend>";
	            	echo "<label for= \"Title\">Title:</label><input name = \"title\" class=\"try\" type = text required/>";
	            	echo "<label for= \"Author\">Author:</label><input name = \"author\" class=\"try\" type = text required/><br>";
	            	echo "<label for= \"Edition\">Edition:</label><input name = \"edition\" class=\"try\" type = text required/>";
	            	echo "<label for= \"ISBN\">ISBN:</label><input name = \"isbn\" class=\"try\" type = text required/><br>";
			echo '<label for= "Condition">Condition:</label>
				<select required name="condition" class="try" id="cond">
					<br><pre><option selected value="">Select a condition</option></pre>
					<option value="Poor">Poor</option>
					<option value="Fair">Fair</option>
					<option value="Good">Good</option>
					<option value="Very Good">Very Good</option>
					<option value="Like New">Like New</option>
					<option value="Brand New">Brand New</option>
				</select><br>';
	            	echo '<label for= "School">School:</label><select required name = "school" class="try" id="form-json-one">
					<br><pre><option selected value="">Select a school</option></pre>
					<option value="ASE">Arts Sciences and Engineering</option>
					<option value="Simon">Simon School of Business Administration</option>
					<option value="Warner">Warner School of Education</option>
					<option value="Eastman">Eastman School of Music</option>
					<option value="Medicine">School of Medicine and Dentistry</option>
				      </select><br>';
			echo '<label for= "Course">Course:</label><select required name="course" class="try" id="form-json-two" >
					<option selected="selected">Select a school above</option>
				      </select><br>';
	            	echo "<label for= \"CourseNumber\">Course Number (e.g. 210):</label><input name = \"courseNum\" class=\"try\" type = number min = \"0\" required/><br>";
// 	            	echo "<label for= \"Photo\">Photo (link to a photo):</label><input name = \"photo\" class=\"try\" type = text required/><br>";
	            	echo '<input type="file" id="pic" name="uploadedfile" accept="image/*" required /><br>';
	            	echo '<img id="previewPic" src="#" alt="uploadPic" style="display:none; width:160px; height:160px;"/>';
	            	echo '<button type="button" id="upload">Upload</button><button type="button" id="remove">Remove</button>';
	            	echo '<div id="preview"></div>';
	            	echo "<label for= \"Price\">Price (enter number):</label><input name = \"price\" class=\"try\" type = number step = \"0.01\" min = \"0\" required/><br>";
	            	echo "<label for= \"Other notes\">Other notes:</label><input name = \"othernotes\" class=\"try\" type = text /><br>";
	            	echo "<input name = \"submit\" type = submit value = \"Sell a Textbook!\" />";
	            	echo '<input name = "reset" type="reset" value="Reset" disabled="true">';
	            	//echo "<input name=\"submit\" type=\"button\" value = \"Sell a Textbook!\" onClick=\"submitForm();\" />";
	            	echo "</fieldset>";
	            	
	            	echo "</form><br><br>";
		}
		?>
	            </div>
	        <div id = "searchpost" style="width: 800px;">
	        <center><div id='pages'></div></center>
	            <div id = "showing"></div>
            	    <div id = "bookpost" style="width: 800px;"></div>
            	</div>
            </div>
            <div id="left" class="column">
            	<label for= "class" accesskey="c">Class</label>
				<select id="json-one">
					<br><pre><option selected value="">Please Select a school</option></pre>
					<option value="ASE">Arts Sciences and Engineering</option>
					<option value="Simon">Simon School of Business Administration</option>
					<option value="Warner">Warner School of Education</option>
					<option value="Eastman">Eastman School of Music</option>
					<option value="Medicine">School of Medicine and Dentistry</option>
				</select>
	
				<br/>
				<form method="post" >
				<select id="json-two" name="courseNum">
					<option>Please choose from above</option>
				</select>
				<input type="button" value="Search" onClick="load()"></input>
				</form>
				<br><br>
				<div
  class="fb-like"
  data-share="true"
  data-width="350"
  data-show-faces="true">
</div>
			 </div>
             <div id="right" class="column">
           	<?php
		$cookie_name = "sessionID";
		if(!isset($_COOKIE[$cookie_name])) {
           		echo "Or <a id='signup' href = \"form.py\">Create an Account</a>";
           	}?>
             </div>
    	</div>
        <div id="footer-wrapper">
              <div id="footer"></div>
        </div>
        <div id='show'><button id="close" class="close">&times;</button></div>
  
</body>
</html>