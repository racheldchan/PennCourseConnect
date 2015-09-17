/*

map.js

This file contains all of the google map api required code

*/

var map;
function initialize() {
    var mylatlng = new google.maps.LatLng(39.951823, -75.191255);
    var mapOptions = {
    center: { lat: 39.9538, lng: -75.5900},
    zoom: 16
	};

	var contentString =
		"<div id='personal-popup'>"+
			"<div id='siteNotice'></div>"+
			"<h1 id='firstHeading' class='firstHeading'>Sahil Shah</h1>"+
			"<div id='bodyContent'>"+
				"<img border='0' align:'left' src='profileSahil.png';>"+
				"<p style='text-align:right'><b>Currently Working On:</b> <input type='text'name='curCourse'></p>"+
				"<p style='text-align:right'><b>Currently in Room:</b> <input type='text' name='curRoom'></p>"+
				"<p style='text-align:right'><b>Having Difficulty With:</b> <input type='text' name='curAssignment''></p>"+
				"<input id='update-button' type='button' onclick='getUpdates()' value='Update'>"+
			"</div>"+
		"</div>";

	map = new google.maps.Map(document.getElementById('map-canvas'),
	            mapOptions);
  var infowindow;
  var marker;

  // Try HTML5 geolocation
  if(navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
      var pos = new google.maps.LatLng(position.coords.latitude,
                                       position.coords.longitude);

      marker = new google.maps.Marker({
            position: pos,
            map: map,
            title: "Sahil Shah"
        })

      infowindow = new google.maps.InfoWindow({
        map: map,
        position: pos,
        content: contentString
      })

        makeInfoWindowEvent(map, infowindow, "test", marker);;

      map.setCenter(pos);
    }, function() {
      handleNoGeolocation(true);
    });
  } else {
    // Browser doesn't support Geolocation
    handleNoGeolocation(false);
  }
	      
}

var getUpdates = function () {
	var curRoom = $("input[name=curRoom]").val();
	var curCourse = $("input[name=curCourse]").val();
	var curAssignment = $("input[name=curAssignment]").val();

	$.ajax({
		type: 'POST',
		url: 'http://localhost:8000/new',
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
}

function handleNoGeolocation(errorFlag) {
  if (errorFlag) {
    var content = 'Error: The Geolocation service failed.';
  } else {
    var content = 'Error: Your browser doesn\'t support geolocation.';
  }
  var options = {
    map: map,
    position: new google.maps.LatLng(60, 105),
    content: content
  };

  var infowindow = new google.maps.InfoWindow(options);
  map.setCenter(options.position);
  }

function makeInfoWindowEvent(map, infowindow, contentString, marker) {
  	google.maps.event.addListener(marker, 'click', function() {
    infowindow.open(map, marker);
  	});
}

google.maps.event.addDomListener(window, 'load', initialize);