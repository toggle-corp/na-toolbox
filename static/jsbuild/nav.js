'use strict';

$(document).ready(function () {
    $('#menu-button').click(function () {
        $('#modal-fill').show();
        $('main').hide();
    });
    $('#modal-close').click(function () {
        $('#modal-fill').hide();
        $('main').show();
    });
});