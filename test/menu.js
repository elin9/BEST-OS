$(document).ready(function(){
	console.log("menu ready!");
		
		$("#json-one").change(function() {
				
				var $dropdown = $(this);
					
				$.getJSON("http://test.elin9.rochestercs.org/data.json", function(data) {
					console.log("json loaded");
					var key = $dropdown.val();
					var vals = [];
										
					switch(key) {
						case 'ASE':
							vals = data.ASE.split(",");
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
		
		
		$("#form-json-one").change(function() {
			
				var $dropdown = $(this);
					
				$.getJSON("http://test.elin9.rochestercs.org/data.json", function(data) {
					console.log("json loaded in form");
					var key = $dropdown.val();
					var vals = [];
										
					switch(key) {
						case 'ASE':
							vals = data.ASE.split(",");
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
					
					var $jsontwo = $("#form-json-two");
					$jsontwo.empty();
					$.each(vals, function(index, value) {
						$jsontwo.append("<option>" + value + "</option>");
						// console.log(value);
					});
			
				});
		});
});