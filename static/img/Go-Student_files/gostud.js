var GOSTUD_URL = "";
//this are the variables
var light = new Array();
var t;
var colorName;
var color=0;
var flipping=0;
var speed=1000;

$("document").ready(function() {
    GOSTUD_URL = $("#GOURL").val()+"/";
});

function clearMsg(obj){
    $(obj).html("");
   
}
     
//the different colors for flipping
    light[0] = 'brown';
    light[1] = 'red';
    light[2] = 'brown';
    light[3] = 'red';
    light[4] = 'brown';

function autoFlip() {
    $("#numberOfUnreadNotices").css('background-color', light[color]);
    if (color > 2) {
        color--;
    }
    else {
        color=light.length-1;
    }
    t = setTimeout("autoFlip(speed)",speed);
}

function doAutoFlip(changespeed){
    if (!flipping){
        flipping=1;
        speed=changespeed;
        autoFlip();
    }
}
        
function changeAySem(){
    var cur_sem = $("#cur_sem").val();
    var cur_year = $("#cur_year").val();
    var url = $("#url").val();
   
    loadingPageOn();
    
    $.ajax({
        url : GOSTUD_URL + "user/ay_sem",
        data : {
            sem : cur_sem,
            year : cur_year,
            _token: $('meta[name="csrf-token"]').attr('content')
        },
        datatype : "json",
        type : 'get',
        success : function(result) {
            $(location).attr('href',GOSTUD_URL+url);
        },
        error : function() {
            alert("Error reaching the server. Check your connection");
            loadingPageOff();
        }
    });
}

function loadingPageOn(){
    //$('#loading-image').addClass("loading");  \
//    if($('.page-loader')[0]) {
//        $('.page-loader').fadeOut();
//    }
    $("#processLoader").html('<div class="page-loader palette-Blue bg"><div class="preloader pl-xl pls-white"><svg class="pl-circular" viewBox="25 25 50 50"><circle class="plc-path" cx="50" cy="50" r="20"/></svg></div></div>');
}

function loadingPageOff(){
     $('.page-loader').fadeOut();
}