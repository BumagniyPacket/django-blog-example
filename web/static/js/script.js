$(window).on("load", function () {
    var $preloader = $("#page-preloader"),
        $spinner   = $preloader.find(".spinner");
    $spinner.fadeOut();
    $preloader.delay(350).fadeOut("slow");
});

// search form
$(".search-wrapper").hide();
$(".search-field").focusout(function() {
    $(".search-icon").show();
    $(".search-wrapper").hide();
});

$(".search-icon").click(function() {
    $(".search-icon").hide();
    $(".search-wrapper").fadeIn(200);
    $(".search-field").focus();
    $(".search-field").val("");
});

// fix menu after scrolling
var num = 40; //number of pixels before modifying styles
$(window).bind("scroll", function () {
    if ($(window).scrollTop() > num) {
        $(".menu").addClass("fixed");
    } else {
        $(".menu").removeClass("fixed");
    }
});
