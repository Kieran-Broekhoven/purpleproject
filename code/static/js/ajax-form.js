$(function() {

    // Get the form.
    var form = $('#contact-form');

    console.log("Setup?");
    // Set up an event listener for the contact form.
    $(form).submit(function(e) {
        e.preventDefault();
        var formData = $(form).serialize();

        console.log("Submit", formData);
        document.body.style.cursor='wait';
        $.ajax({
            type: 'POST',
            url: '/api/sendMail/',
            data: formData
        })
        .done(function(response) {
            // Clear the form.
            // $('#contact-form input,#contact-form textarea').val('');
            alert("Thank you for your message!")
        })
        .fail(function(data) {
            console.log("FAIL!");
            alert("Failed to send");
        }).always(function(e){
            document.body.style.cursor='default';
        });
    });

});
