$('input[type="checkbox"]').on('change', function() {
   $(this).siblings('input[type="checkbox"]').prop('checked', false);
});

$(document).ready(function() {
	$('#change-birthday-input ').click(function() {
		$('#birthday-input').css({display: 'block'});
	});
});