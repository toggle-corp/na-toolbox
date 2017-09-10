$(document).ready(function() {
    $('.open-select select').on('change', function() {
        if ($(this).val() == 'other') {
            console.log('gg wp');
            $(this).closest('.input-group').find('input').slideDown();
        } else {
            $(this).closest('.input-group').find('input').slideUp();
        }
    });

    $('.open-checkbox input[type="checkbox"]').on('change', function() {
        if ($(this).val() == 'other') {
            if($(this).prop('checked')) {
                $(this).closest('.input-group').find('input[type="text"]').slideDown();
            } else {
                $(this).closest('.input-group').find('input[type="text"]').slideUp();
            }
        }
    });
});
