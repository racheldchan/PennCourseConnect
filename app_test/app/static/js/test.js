/**
* jQuery Document Ready function:  when the page loads, these functions will execute.
*
*/
$(document).ready(function () {

	if (localStorage['signedIn'] === 'true') {
		//user has logged in
		$("#login").hide();
		$("#signup").hide();

	}

	// temp database of classes
	var classData = multiGet('http://cis197.herokuapp.com/departmentURLs.json',
                            'http://cis197.herokuapp.com/');
    var triePromise = trieFromDataPromise(classData);
  	var courseSearch = new AppView($('#course-search'), $('#item-template').html(), triePromise, '#course-input', '#course-suggestions-list', 'course');
  	var filterSearch = new AppView($('#course-filter-search'), $('#item-template').html(), triePromise,
  		'#course-filter-input', '#course-filter-suggestions-list', 'course-filter');

	$('#login').on('click', function () {
		localStorage['signedIn'] = true;
	});

	$('#logout').on('click', function () {
		localStorage['signedIn'] = false;
		$("#login").show();
		$("#signup").show();
	});

	$('#signup-button').on('click', function() {
		$('#signup-form').toggle(500);
	});

	var classes = "";
	var courseNum = 1;


	$('#add-class').on('click', function() {
		var c = $('input[name=course]').val();

		$('#courseKart').append("<li class='course-kart-item' id='course" + courseNum + "'>" + c +
			"<div class='remove-course-from-kart' id='remove-course-" + courseNum + "'>x</div></li>");

		var cur = courseNum;

		$('#remove-course-' + cur).on('click', function() {
			$('#course' + cur).remove();
		});

		courseNum++;

		classes += c + ";";

		$('#course-input').val("");
	});

	$('#submit-button').on('click', function() {
		var fname  = $("input[name=fname]").val();
		var lname  = $("input[name=lname]").val();
		var uname  = $("input[name=uname]").val();
		var email  = $("input[name=email]").val();
		var pword  = $("input[name=pword]").val();
		var gender = $("input[name=radios]").val();
		var year   = $("input[name=year]").val();
		var major  = $("input[name=major").val();
		var bio    = $("input[name=bio]").val();

		$.ajax({
			type: 'POST',
			url: 'http://localhost:8000/new',
			data: {
				firstName: fname,
				lastName: lname,
				username: fname,
				email: email,
				password: pword,
				gender: gender,
				classes: classes,
				year: year,
				major: major,
				bio: bio
			},
			async: true,
			success: function(data) {
				//success
			}
		});
	});

	$('#updateCurrent').on('click', function() {
		var curRoom = $("input[name=curRoom").val();
		var curCourse = $("input[name=curCourse").val();
		var curAssignment = $("input[name=curAssignment").val();

		$.ajax({
			type: 'PUT',
			url: 'localhost:8080/new',
			data: {
				currentCourse: curCourse,
				currentRoom: curRoom,
				currentAssignment: curAssignment
			},
			async: true,
			success: function(data) {
				//success
			}
		});
	});
});
