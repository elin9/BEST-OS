$(document).ready(function(){
	console.log("ready!");
		
		$("#json-one").change(function() {
			
				var $dropdown = $(this);
			
				$.getJSON("http://elin9.rochestercs.org/cgi-bin/data.json", function(data) {
				
					var key = $dropdown.val();
					var vals = [];
										
					switch(key) {
						case 'Art':
							vals = data.Art.split(",");
							break;
						case 'Simon':
							vals = data.Simon.split(",");
							break;
						case 'Warner':
							vals = data.Warner.split(",");
							break;
						case 'Eastman':
							vals = data.Eastman.split(",");
							break;
						case 'Medicine':
							vals = data.Medicine.split(",");
							break;
						case 'base':
							vals = ['Please choose from above'];
					}
					
					var $jsontwo = $("#json-two");
					$jsontwo.empty();
					$.each(vals, function(index, value) {
						$jsontwo.append("<option>" + value + "</option>");
					});
			
				});
			});
});