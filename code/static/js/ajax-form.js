$(function() {

	// Get the form.
	var form = $('#contact-form');

	// Get the messages div.
	var formMessages = $('.ajax-response');

	console.log("Setup?");
	// Set up an event listener for the contact form.
	$(form).submit(function(e) {
		// Stop the browser from submitting the form.
		e.preventDefault();

		// Serialize the form data.
		var formData = $(form).serialize();

		console.log("Submit", formData);
		// Submit the form using AJAX.
		$.ajax({
			type: 'POST',
			// url: $(form).attr('action'),
			url: '/api/sendMail',
			data: formData
		})
		.done(function(response) {
			// Make sure that the formMessages div has the 'success' class.
			$(formMessages).removeClass('error');
			$(formMessages).addClass('success');

			// Set the message text.
			$(formMessages).text(response);

			// Clear the form.
			// $('#contact-form input,#contact-form textarea').val('');
			alert("Thank you for your message!")
		})
		.fail(function(data) {
			// Make sure that the formMessages div has the 'error' class.
			console.log("FAIL!");
			$(formMessages).removeClass('success');
			$(formMessages).addClass('error');

			// Set the message text.
			if (data.responseText !== '') {
				$(formMessages).text(data.responseText);
			} else {
				$(formMessages).text('Oops! An error occured and your message could not be sent.');
			}
		});
	});

});
