$(document).ready(function() {

    $('.checkbox').on('click', function() {
        $(this).toggleClass('checked');
        $(this).addClass('clicked');

        let that = this;
        setTimeout(() => { 
            $(that).find('i').addClass('fading'); 
            setTimeout(() => { 
                $(that).removeClass('clicked'); 
                $(that).find('i').removeClass('fading'); 
            }, 200);
        }, 200);

        if (!$(this).is($('#check-all'))) {
            syncCheckState();
        }


    });

    $('#check-all').on('click', function() {
        if($(this).hasClass('checked')) {
            checkAll();
        } else {
            unCheckAll();
        }
    });


});

function checkAll() {
    $('.checkbox').addClass('checked');
}
 
function unCheckAll() {
    $('.checkbox').removeClass('checked');
}

function syncCheckState() {
    let allChecked = true;
     
    $('.checkbox').not($('#check-all')).each(function() {
        if (!$(this).hasClass('checked')) {
            allChecked = false; 
            return false;
        }
    });

    if (allChecked) {
        $('#check-all').addClass('checked');
    } else {
        $('#check-all').removeClass('checked');
    }
}
