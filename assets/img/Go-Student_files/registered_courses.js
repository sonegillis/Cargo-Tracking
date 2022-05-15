

$("document").ready(function() {

    $("#getCourseBtn").click(getRegCourse); 
});

function getRegCourse(){
    loadingPageOn();
    $("#finalRegCourses").html("<div  class = 'alert alert-warning'>Please Wait ...</div>");  
      
    $.ajax({
        url : GOSTUD_URL + "student/get_reg_courses",
        data : {
            year : $("#year").val(),
            sem : $("#sem").val(),
             _token: $('meta[name="csrf-token"]').attr('content')
        },
        datatype : "json",
        type : 'post',
        success : function(result) {

            console.log(result);
            var rs = JSON.parse(result);

            if (rs.state == "success") {
               
               $("#finalRegCourses").html(rs.finalRegCourses);
               $("#loading").hide();
                }else{
                    alert("An Error Occured. Please try again.");
                    $("#loading").hide();
                    //	$(location).attr('href',"#home");
                    
            }
            
            loadingPageOff();
        },
        error : function() {
            alert("Error reaching the server. Check your connection");
            
            loadingPageOff();
        }
    });
}

function download(){
    $(location).attr('href',GOSTUD_URL + "formb_pdf");
}
