$(document).on('submit', '#hospitality-form', function(e){
    e.preventDefault();

    $.ajax({

        url:'/hospitality/',
        type:'POST',
        data:{
            room: $('#room').val(),
            
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        success:function(){
            $('#hospitality-form').css('display','none');
            Materialize.toast('Submitted!', 3000, 'rounded');
        },
      
    });

});

$(document).on('submit', '#team-form', function(e){
    e.preventDefault();

    $.ajax({

        url:'/team/',
        type:'POST',
        data:{
            number: $('#number').val(),
            
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        success:function(){
            $('#team-form').css('display','none');
            $('#no-of-tema').css('display','block');
            Materialize.toast('Submitted!', 3000, 'rounded');
        },
      
    });

});
