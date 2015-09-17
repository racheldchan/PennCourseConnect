/*

map.js

This file contains all of the google map api required code

*/

var map;
function initialize() {
    var mylatlng = new google.maps.LatLng(41.069717, -73.844799);
    var mapOptions = {
    center: { lat: 41.069717, lng: -73.844799},
    zoom: 16
	};

	map = new google.maps.Map(document.getElementById('map-canvas'),
	            mapOptions);
   
}

google.maps.event.addDomListener(window, 'load', initialize);