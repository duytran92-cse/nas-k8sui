function showPopup(targetHref, closeHook) {
    var popupWidth = jQuery(window).width() * 8 / 10;
    var popupHeight = jQuery(window).height();

    jQuery.fancybox.open({
        openEffect  : 'none',
        closeEffect : 'none',
        href: targetHref,
        type: 'iframe',
        width: popupWidth,
        height: popupHeight,
        autoSize    : false,
        afterClose: function() {
			if (typeof closeHook === 'undefined') {
			}
			else {
				closeHook();
			}
        }
    });
}
