$('#search-form').submit(function(e) {
      $.ajax({
        url: '/ajaxtest',
        data: $('#search-form').serialize(),
        type: 'POST',
        success: function(response) {
          console.log("in ajax thing")
        },
        error: function(error) {
            console.log(error);
        }
    });
});
