$(document).ready(function(){
    $("#Poster").change(function(){
        var request = $.ajax({
            url: "{% url 'Poster_update:edit_poster' %}",
            type: "POST",
            data: { Poster: $("#Poster").val(),
                    csrfmiddlewaretoken: '{{ csrf_token }}'
                  },
            dataType: "html"
        });

        request.done(function(msg) {
                  $("#Poster").html( msg );
        });

    });

});