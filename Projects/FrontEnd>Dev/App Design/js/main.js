;
(function ($) {
	"use strict";

	$(document).on('ready', function () {



		$(document).ready(function () {

			$('.list.one').click(function () {
				if ($('.list.one').hasClass('one') == true) {
					$('.list.one').addClass('active');
					$('.list.two').removeClass('active');
					$('.list.three').removeClass('active');
					$('.list.four').removeClass('active');
					$('.list.five').removeClass('active');
				}
			});
			$('.list.two').click(function () {
				if ($('.list.two').hasClass('two') == true) {
					$('.list.two').addClass('active');
					$('.list.one').removeClass('active');
					$('.list.three').removeClass('active');
					$('.list.four').removeClass('active');
					$('.list.five').removeClass('active');
				}
			});
			$('.list.three').click(function () {
				if ($('.list.three').hasClass('three') == true) {
					$('.list.three').addClass('active');
					$('.list.one').removeClass('active');
					$('.list.two').removeClass('active');
					$('.list.four').removeClass('active');
					$('.list.five').removeClass('active');
				}
			});
			$('.list.four').click(function () {
				if ($('.list.four').hasClass('four') == true) {
					$('.list.four').addClass('active');
					$('.list.one').removeClass('active');
					$('.list.two').removeClass('active');
					$('.list.three').removeClass('active');
					$('.list.five').removeClass('active');
				}
			});
			$('.list.five').click(function () {
				if ($('.list.five').hasClass('five') == true) {
					$('.list.five').addClass('active');
					$('.list.one').removeClass('active');
					$('.list.two').removeClass('active');
					$('.list.three').removeClass('active');
					$('.list.four').removeClass('active');
				}
			});
		});

		//sliderOne
		$('.SliderOne').slick({
			dots: true,
			arrows: false,
			infinite: false,
			autoplay: true,
			infinite: true,
			speed: 300,
			slidesToShow: 2,
			slidesToScroll: 1,
			responsive: [
				{
					breakpoint: 1100,
					settings: {
						slidesToShow: 2,
						slidesToScroll: 1,
					}
                },
				{
					breakpoint: 766,
					settings: {
						slidesToShow: 1,
						slidesToScroll: 1,
					}
                }
		]
		});
		
		//sliderTwo
		$('.SliderTwo').slick({
			dots: true,
			arrows: false,
			infinite: false,
			speed: 300,
			slidesToShow: 3,
			slidesToScroll: 1,
			autoplay: true,
			infinite: true,
		});
		
	});

})(jQuery);
