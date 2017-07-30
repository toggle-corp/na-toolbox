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

        if ($(this).hasClass('check-all')) {
            if($(this).hasClass('checked')) {
                checkAllInSection($(this).closest('section'));
            } else {
                unCheckAllInSection($(this).closest('section'));
            }

        } else {
            syncCheckState();
        }

        updateSelectedCount();
    });

    $('main > .content').scroll(function() {
        syncNavigationTabs();
    });

    $('#navigation-tabs a').on('click', function() {
        let container = $('main').children('.content');
        let target = $('#' + $(this).data('target'));
        container.scrollTop(target.offset().top - container.offset().top + container.scrollTop());
        syncNavigationTabs();
    });
    syncNavigationTabs();
});

function checkAllInSection(sectionSelector) {
    $(sectionSelector).find('.checkbox').addClass('checked');
}

function unCheckAllInSection(sectionSelector) {
    $(sectionSelector).find('.checkbox').removeClass('checked');
}

function checkAll() {
    $('.checkbox').addClass('checked');
}
 
function unCheckAll() {
    $('.checkbox').removeClass('checked');
}

function syncCheckState() {
     
    $('section').each(function() {
        let allChecked = true;
         
        $(this).find('.checkbox').not($('.check-all')).each(function() {
            if (!$(this).hasClass('checked')) {
                allChecked = false; 
                return false;
            }
        });
         
        if (allChecked) {
            $(this).find('.check-all').addClass('checked');
        } else {
            $(this).find('.check-all').removeClass('checked');
        }
    });

}

function updateSelectedCount() {
    $('#selection-count').text($('.checkbox.checked').not($('.check-all')).length);
}

function syncNavigationTabs() {
    let mainOffset = $('main').offset().top + $('main > header').height();
    $('#navigation-tabs a.active').removeClass('active');
         
    $('section').each(function() {
        if( ($(this).offset().top - mainOffset - 2) < 0 && ($(this).offset().top + $(this).height() - mainOffset - 2) > 0) {
            $('#navigation-tabs a[data-target="' + $(this).prop('id') + '"]').addClass('active');
        }
    });
}
