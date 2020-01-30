$('#form').submit(function(e){
    $.post('/url/', $(this).serialize(), function(data){ ... 
       $('.message').html(data.message);
       // of course you can do something more fancy with your respone
    });
    e.preventDefault();
});