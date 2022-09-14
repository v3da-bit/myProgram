$(document).ready(function () {
    var f=0
    $("#fade").click(function () { 
        if(f==0){
            $("#first").fadeOut("slow",f1);
            function f1(){
                $("#second").fadeOut("slow",f2);
            }
            function f2(){
                $("#third").fadeOut("slow");
            }
            f=1
        }
        else{
            $("#first").fadeIn("slow",f1);
            function f1(){
                $("#second").fadeIn("slow",f2);
            }
            function f2(){
                $("#third").fadeIn("slow");
            }
            f=0
            
        }
        
    });
});