$(document).ready(function () {
    $("h2").css("display", "none");
    $("#inp").focus(function () { 
        $("#focusone").css("display", "inline").fadeOut(6000);
        
    });
    $("#inp").blur(function () { 
        $("#ṇblurone").css("display", "inline").fadeOut(6000);
        
        
    });
});