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
        syncTabPositionOnScroll();
    });

    $('#navigation-tabs a').on('click', function() {
        let container = $('main').children('.content');
        let target = $('#' + $(this).data('target'));
        container.scrollTop(target.offset().top - container.offset().top + container.scrollTop());
        syncNavigationTabs();
    });
    syncNavigationTabs();

    $('#download-selected').click(function() {
        downloadSelected();
    });

    calculateNavigationWidth();
    syncScrollButtons();

    $(window).on('resize', () => {
        syncScrollButtons();
    });
});

function calculateNavigationWidth() {
    let navigationTabs = $('#navigation-tabs');
    let container = navigationTabs.find('.scroll-wrapper');

    let totalWidth = 0;
    container.find('a').each(function() {
        totalWidth += $(this).outerWidth();
    });

    container.width(totalWidth);
}

function syncScrollButtons() {
    let navigationTabs = $('#navigation-tabs');
    let scrollWrapper = navigationTabs.find('.scroll-wrapper');

    if (navigationTabs.scrollLeft() > 0) {
        $('#scroll-left-btn').show();
    } else {
        $('#scroll-left-btn').hide();
    }

    if (navigationTabs.scrollLeft() < (scrollWrapper.width() - navigationTabs.width() - 1 )) {
        $('#scroll-right-btn').show();
    } else {
        $('#scroll-right-btn').hide();
    }

}

function syncTabPositionOnScroll() {
    let navigationTabs = $('#navigation-tabs');
    let scrollWrapper = navigationTabs.find('.scroll-wrapper');
    let activeItem = scrollWrapper.find('.active');

    if (activeItem.length > 0) {
        let startPosition = activeItem.position().left;
        let endPosition = startPosition + activeItem.outerWidth();
        let diff = endPosition - navigationTabs.width();

        if (diff > 0) {
            navigationTabs.scrollLeft(navigationTabs.scrollLeft() + diff);
            syncScrollButtons();
        }

        diff = startPosition - navigationTabs.position().left - 32;
        if (diff < 0) {
            navigationTabs.scrollLeft(navigationTabs.scrollLeft() + diff);
            syncScrollButtons();
        }
    }
}

function scrollNavTabRight(animate=true) {
    let navigationTabs = $('#navigation-tabs');
    if (animate) {
        navigationTabs.animate({scrollLeft: '+=100'}, 200, () => { syncScrollButtons(); });
    } else {
        navigationTabs.scrollLeft(navigationTabs.scrollLeft() + 100);
        syncScrollButtons();
    }

}

function scrollNavTabLeft(animate=true) {
    let navigationTabs = $('#navigation-tabs');
    if (animate) {
        navigationTabs.animate({scrollLeft: '-=100'}, 200, () => { syncScrollButtons(); });
    } else {
        navigationTabs.scrollLeft(navigationTabs.scrollLeft() - 100);
        syncScrollButtons();
    }

}

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


function downloadSelected() {
    let selectedUrls = $('.tool .checkbox.checked').map(function() {
        return $(this).closest('.tool').data('url');
    }).get();

    $('form').find('input[name="urls"]').val(JSON.stringify(selectedUrls));

    const targetName = 'downloadWindow-' + (Date.now()) + '-' + String(Math.floor(Math.random() * 9e15));
    $('form').attr('target', targetName);

    const popup = window.open(DOWNLOADING_URL, targetName);
    popup.onload = function() {
        $('form').submit();
    };
}
