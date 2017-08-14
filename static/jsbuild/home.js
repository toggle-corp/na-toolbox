'use strict';

$(document).ready(function () {
    var slideActiveDuration = 5000;
    //let nextSlideTimeout = setTimeout(() => { showNextCarouselItem('#intro-container .carousel'); }, slideActiveDuration);

    $('.carousel-navigation button').on('click', function () {
        //clearTimeout(nextSlideTimeout);

        $(this).siblings('.active').removeClass('active');
        $(this).addClass('active');

        var itemsContainer = $(this).closest('.carousel').find('.carousel-item-container');
        showCarouselItem(itemsContainer.find($(this).data('target')));

        //nextSlideTimeout = setTimeout(() => { showNextCarouselItem('#intro-container .carousel'); }, slideActiveDuration);
    });

    function showCarouselItem(item) {
        item.siblings('.carousel-item.active').hide().removeClass('active');
        item.show().addClass('active');
    }

    $('#intro-container .carousel-navigation button').eq(0).click();

    function showNextCarouselItem(carouselSelector) {

        var navigationContainer = $(carouselSelector).find('.carousel-navigation');
        var current = navigationContainer.find('.active');
        var next = current.next();

        if (next.length === 0) {
            next = current.siblings().eq(0);
        }

        next.click();
    }
});
//# sourceMappingURL=home.js.map