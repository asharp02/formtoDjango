        $("#id_PDFPoster").change(function () {
        var first_name = $("input[name=first_name]").val();
        var last_name = $("input[name=last_name]").val();   
        var year = $('input[name="Year"]:checked').val();
        var semester = $('input[name="Semester"]:checked').val();
        var course = $('input[name="Course_name"]:checked').val();
        var year_range
        if (semester == "Spring"){
            var first_year = year - 1
            year_range = String(first_year) + "-" + String(year)
        }else{
            next_year = parseInt(year)+1
            year_range = String(year) + "-" + String(next_year)
        }
        var course_code = String(course).substring(0, String(course).indexOf("_"))

        if (first_name != "" && last_name != "" && year != null && semester != null && course != null){
            document.getElementById("posterpath").innerHTML = "The poster will be saved at: " + "S:/Posters/GIS Posters/" + year_range + "/" +
            "PostersComplete" + semester + year + "/" + course + "/" + last_name + "_" + first_name + "_" + course_code + "_" + year + ".pdf";
        }
     });

             {% for field in form %}
            <br><div class="label_tag">{{field.label_tag}}</div>
             <div class="help_text">{{field.help_text}}</div>
             {{field}}<br>
    {% endfor %}

