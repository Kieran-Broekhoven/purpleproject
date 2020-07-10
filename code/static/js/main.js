(function ($) {
"use strict";

// TOP Menu Sticky
$(window).on('scroll', function () {
	var scroll = $(window).scrollTop();
	if (scroll < 100) {
    $("#sticky-header").removeClass("sticky");
    $('#back-top').fadeIn(500);
	} else {
    $("#sticky-header").addClass("sticky");
    $('#back-top').fadeIn(500);
	}
});

$(document).ready(function(){
  $("#headerArea").load('/static/header.html', function(){
    let path = window.location.pathname.replace(new RegExp("^[/]+"), "").replace(new RegExp("[/]+$"), "");
    if(!path){
      path = 'index';
    }
    else if (path === 'info' || path === 'impact') {
      path = 'menu';
    }
    $('#'+path+'Tab').addClass('active');
  });
  // mobile_menu
  var menu = $('ul#navigation');
  if(menu.length){
    menu.slicknav({
      prependTo: ".mobile_menu",
      closedSymbol: '+',
      openedSymbol:'-'
    });
  };
  // $('#donateBtn').on('click', function(){
  //   console.log('SUBMIT!');
  //   $('#donateForm').submit();
  //   console.log("Submitted");
  // });
  // $('#donateBtn').click(function(){
  //   $('#donateForm').submit();
  // })
  // $("#headerVideoLink").on("click", function(e) {
  //   e.preventDefault();
  //   var $this = $(this);
  //   var videoUrl = $this.attr("data-media");
  //   var popup = $this.attr("href");
  //   var $popupIframe = $(popup).find("iframe");

  //   $popupIframe.attr("src", videoUrl);

  //   $this.closest(".video_bg_1").addClass("show-popup");
  // });

  // $(".popup").on("click", function(e) {
  //     e.preventDefault();
  //     e.stopPropagation();

  //     $(".video_bg_1").removeClass("show-popup");
  // });

  // $(".popup > iframe").on("click", function(e) {
  //     e.stopPropagation();
  // });
  // $('#headerVideoLink').magnificPopup({
  //   type:'inline',
  //   midClick: true // Allow opening popup on middle mouse click. Always set it to true if you don't provide alternative source in href.
  // });         
});
   
})(jQuery);	