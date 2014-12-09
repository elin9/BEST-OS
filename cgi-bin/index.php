<!DOCTYPE html>

<html>
<head>
<title>Home</title>
<link rel = "stylesheet" type = "text/css" href="http://elin9.rochestercs.org/experimenting/style2.css">
<link rel = "stylesheet" type = "text/css" href="http://elin9.rochestercs.org/experimenting/simplePagination.css">
<script src="http://elin9.rochestercs.org/jquery-1.11.0.js"></script>
<script src="http://elin9.rochestercs.org/menu.js"></script>
<script src="http://malsup.github.com/jquery.form.js"></script> 
<script src="http://elin9.rochestercs.org/jquery.cookie.js"></script>
<script src="http://elin9.rochestercs.org/jpaginate.js" type="text/javascript"></script>

<script type="text/javascript">
var photolink="";
$(document).ready(function() {
  console.log("Loaded!");
  $('#bookpost').load('printTextbook.py',function(){
    			showpage($(this).find($('.post')));
				
  });
  
  $('#json-one').change(function(){
	console.log("the user has selected a school");
	$('#json-two').attr('size',20)
	.css({"height": "200px", "margin":"0.5em 0 0.5em 0"});
  });
  
  $('input[type="text"],textarea').keyup(function(){
  	$('input[name="clear"]').attr('disabled',false);
  	$('input[name="clear"]').click(function(){
		$('#form-json-two').val('Please choose from above');
		$('#previewPic').hide();
  	});
  });
  
  $('#form-json-one').change(function(){
	console.log("school selected in bookposts form");
  });
  
  //----------------------------
  $('#previewPic[src="#"]').hide();
  $('#previewPic:not([src="#"])').show();
 $('#pic').change(function(){
    $('#previewPic').toggle();
  	readURL(this); //preview the pic and get the url
  });
  
//   $('input[value="Sell a Textbook!"]').click(function(){
//   		console.log("happy upload");
//   		var file = $('#previewPic').attr('src');
//   		var title = $('#postsomething').find('input[name="title"]').val();
//   		var user = $.cookie("name");
// 		var fd = new FormData();
//     	fd.append("file",file);
// 		$.ajax(
// 		{
//         	url: "http://elin9.rochestercs.org/upload.php",
//         	type: "POST",
// 			contentType: false,
// 			processData: false,
//         	data: fd,
// 
//         	success: function(data) {
//         		console.log(data);
// 				photolink = 'http://elin9.rochestercs.org/'+data;
// 				console.log('uploaded'+photolink);
//         	}, 
//   		});
// 	});
// 	


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
  	upload().done(function(r){
  		var photoo = 'http://elin9.rochestercs.org/'+r;
  		console.log('works'+photoo);
  		var user = $.cookie("name");
        var title = $('#postsomething').find('input[name="title"]').val();
        var author = $('#postsomething').find('input[name="author"]').val();
        var edition = $('#postsomething').find('input[name="edition"]').val();
        var isbn = $('#postsomething').find('input[name="isbn"]').val();
        var condition = $('#postsomething').find('select[name="condition"]').val();
        var otherNotes = $('#postsomething').find('textarea[name="othernotes"]').val();
        var school = $('#postsomething').find('select[name="school"]').val();
        var course =$('#postsomething').find('select[name="course"]').val();
        var courseNum = $('#postsomething').find('input[name="courseNum"]').val();
        var photoo = photolink;
        var price = $('#postsomething').find('input[name="price"]').val();
	 	$.ajax(
      {
        url: "http://elin9.rochestercs.org/cgi-bin/postTextbook.py",
        type: "POST",
        dataType: "text",
        data: {user: user, title: title, author: author, edition: edition, isbn: isbn, condition: condition, othernotes: otherNotes, school: school, course: course, courseNum: courseNum, photo: photoo, price: price},

        success: function(data) {
          console.dir(data);
          submitForm();
          $("#bookpost").load("printTextbook.py");
          //$("#bookpost").prepend("<div class = \"post\" style = \"border: 1px solid #000000; height: 100px;\">Seller: " + user+ " | Title: " + title + " | Author: " + author + " | Edition: " + edition + " | ISBN: " + isbn + " | Condition: " + condition + " | Other Notes: " + otherNotes + " | Course Number: " + courseNum + "<img style = \"width: 50px; height: 70px; float: left;\" src = \""+photo+"\"> | Price: $" + price + " | School: " + school + " | Course: " + course + "</div><br><br>");
          console.log("book posted!");
          //window.location.replace('http://elin9.rochestercs.org/cgi-bin/index.php');
        },
      }
    );
    
  	})
  	.fail(function(){
  		console.log('failed');
  	});
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
          //window.location.replace('http://elin9.rochestercs.org/cgi-bin/index.php');
          if ($.cookie("name") === undefined){
             $("#right").append(data + "<br>");
          } else{
             console.log("logged in!");
             $("#right").append("Hi, " + data + "!<br>");
             $("#right").append("You are now logged in.<br>");
             window.location.replace('http://elin9.rochestercs.org/cgi-bin/index.php');
          }
        },
      }
    );
  });

});

function load()
{
  var school = $("#json-one").val();
  var course = $("#json-two").val();
  var searchString = school + " " + course;
  $("#showing").html("Showing textbooks for " + searchString + ":<br><br>");
  $("div.post:not(:contains('"+searchString+"'))").hide();
  $("div.post:contains('"+searchString+"')").show("fast");
  showpage($("div.post:contains('"+searchString+"')"));
  if(!$("div.post:contains('"+searchString+"')").show().length){
  	$('#showing').addClass('nopost').html(
  	"<table>Sorry there were no matching posts<br>"+
  	"Click to go back and see all posts<br>"+
  	"<button id='goback'>All Posts</button></table>");
  	$('#goback').click(function(){
  		$('#showing').hide();
  		showpage($('#bookpost .post'));
  		$('#bookpost .post').show("fast");
  	});
  }else{
  		$('#showing').removeClass('nopost').show();
  }
				
}

function upload(){
	console.log("happy upload");
  	var file = $('#previewPic').attr('src');
  	var title = $('#postsomething').find('input[name="title"]').val();
  	var user = $.cookie("name");
	var fd = new FormData();
    fd.append("file",file);
	return $.ajax(
	{
        url: "http://elin9.rochestercs.org/upload.php",
    	type: "POST",
		contentType: false,
		processData: false,
       	data: fd,
<!-- 

     	success: function(data) {
        		console.log(data);
				photolink = 'http://elin9.rochestercs.org/'+data;
				
        }, 
 -->
  	});
}

function submitForm()
{
   	var r = confirm("successfully posted! Do you want to sell another textbook?");
	if (r == true) {
   		document.forms["bookpostform"].reset();
   		$('#previewPic').hide();
	} else {
		document.forms["bookpostform"].reset();
   		$('#previewPic').hide();
		$('#postform').hide();
	}
}

function posted() 
{
	return confirm('You have posted a textbook!');
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

//----------------------------
function showpage(data){
	var showperpage = 5; 
    			var post = data;
				var totalContent = post.length;

				data.slice(showperpage).hide();
				
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
}


</script>
</head>
<body>
	<div id="header">
		<div id ="banner" style = "z-index:1;">
			<a href = "http://elin9.rochestercs.org/cgi-bin/index.php"><img src="http://elin9.rochestercs.org/img/bann.png"/></a>
		</div>
	 	<div id = "loginbox">
		 	<?php
			$cookie_name = "sessionID";
			if(!isset($_COOKIE[$cookie_name])) {
			    echo "<form id = \"login\" method = post action = \"login2.py\">";
			    echo "Username: <input name=\"username\" type=text size=\"20\" required/><br> ";
			    echo "Password: &nbsp;<input name=\"password\" type=password size=\"20\" required/>";
			    echo "<input type = submit name = \"submit\" value = \"Login\"/></form><br>";
			} else {
			    //echo "<form style = \"display: inline;\" method = post action = \"http://elin9.rochestercs.org/cgi-bin/deleteUser.py\">";
			    //echo "<input type=submit name = \"delete\" value = \"Delete your account\"></form> ";
			    echo "<form style = \"display: inline;\" method = post action = \"http://elin9.rochestercs.org/cgi-bin/editSettings.php\">";
			    echo "<input type=submit name = \"usersettings\" value = \"Account Settings\"></form> ";
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
				?>
   				<form id = "postsomething" name = "bookpostform" method = post >
                <h5 align='center'>Enter in the following information about the textbook you want to sell:</h5>
				<table id="t" width="90%" align="center">
				<tr>
					<td width="5%"><label for= "Title">Title:</label></td><td width="25%"><input name = "title" class="try" type = text required/></td> 
					<td width="5%"><label for= "Author">Author:</label></td><td  width="15%"><input name = "author" class="try" type = text required/></td>
				</tr>
				<tr>
					<td><label for= "Edition">Edition:</label></td><td><input name = "edition" class="try" type = text required/></td>
					<td><label for= "ISBN">ISBN:</label></td><td><input name = "isbn" class="try" type = text required/></td>
				</tr>
				<tr>
					<td><label for= "Condition">Condition:</label></td>
					<td><select style="width:140px;" required name="condition" class="try" id="cond">
					<pre><option selected value="">Select a condition</option></pre>
					<option value="Poor">Poor</option>
					<option value="Fair">Fair</option>
					<option value="Good">Good</option>
					<option value="Very Good">Very Good</option>
					<option value="Like New">Like New</option>
					<option value="Brand New">Brand New</option>
				</select></td>
                    <td><label for= "Course">Course:</label></td>
					<td width="5%"><select required name="course" class="try" id="form-json-two" >
					<option selected="selected">Select a school above</option>
				      </select></td>
				</tr>
				<tr>
					<td><label for= "School">School:</label></td>
					<td><select style="width:140px;" required name = "school" class="try" id="form-json-one">
					<pre><option selected value="">Select a school</option></pre>
					<option value="ASE">Arts Sciences and Engineering</option>
					<option value="Simon">Simon School of Business Administration</option>
					<option value="Warner">Warner School of Education</option>
					<option value="Eastman">Eastman School of Music</option>
					<option value="Medicine">School of Medicine and Dentistry</option>
				    </select></td>
				
				    <td  width="18%"><label for= "CourseNumber">
				      Course Number (e.g. 210):</label>
				      </td><td><input type="number" step="1" style="width:50px;" name = "courseNum" class="try" min = "1" max="999" required/></td>
				</tr>
				<tr>
					<td><label>Please upload a book cover:</label><input style="width:80px;" type="file" id="pic" name="uploadedfile" accept="image/*" required /></td>
					<td rowspan="2"><img id="previewPic" src="#" alt="uploadPic" style="display:none; width:160px; height:160px; border=1px solid #aaa;"/><div id="preview"></div></td>
					<td colspan="2" rowspan="4">
						<table width="100%">
							<tr><td width="45%"><label for= "Price">Price:</label></td>
						    <td><input name = "price" class="try" type = number step = "0.01" min = "0" required/></td></tr>
							<tr><td><label for= "Other notes">Other notes:</label></td></tr>
							<tr><td colspan="3"><textarea name = "othernotes" class="try" type = text ></textarea></td></tr>         
							<tr><td><center><input name = "submit" type = submit onSubmit="return posted();"value = "Sell a Textbook!" /><input name = "clear" type="reset" value="Reset" disabled="true"></center></td></tr>
						</table>
					</td>
				</tr>
				
				</table>
           		</form><br><br>
           	
			<?php
			}
			?>
	            </div>
	        <div id = "searchpost" style="width: 800px;">
	        	 <div id='pages'></div>
	            <div id = "showing"></div>
            	    <div id = "bookpost" style="width: 800px;"></div>
            	</div>
            </div>
            <div id="left" class="column">
            	<label for= "class" accesskey="c">Select a Course</label>
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