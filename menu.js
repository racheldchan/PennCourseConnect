/*

menu.js

This file controls the frontend animations and interactions with the main menu.

*/

$(document).ready(function () {

	// keep track of whether the menu is extened--or "out"--or closed
	var out = false;
	
	// on hover, menuRow cells will look highlighted
	$('.menuRow').hover(function () {
		$(this).css('background-color', '#e0e0e0');
	}, function () {
		$(this).css("background-color", "#EEE");
	});

	// bind a rotation animation to the menu icon on clicks
	$("#menuPic").rotate({bind:{
		click: function() {
			if (out) {
				$(this).rotate({
					duration:750,
					angle:-90,
					animateTo:0
				})
			} else {
				$(this).rotate({
					duration:750,
					angle:0,
					animateTo:-90
				})
			}
		}
	}});

	// bind a pop-out animation to the menu-container when the menu icon is clicked
	$("#menuPic").on("click", function() {
		if (out) {
			$('#menu-container').animate({
				height: "-=220",
				width: "-=100"
				}, 500);
		} else {
			$('#menu-container').animate({
    			height: "+=220",
    			width: "+=100"
  				}, 500);
		}
		out = !out;
		//$("#menuTitle").toggle(400);
		$('.menuRow').toggle(500);
	});
	
});