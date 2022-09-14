$(document).ready(function () {
    var s=0
   $("#b2").click(function () { 
    
    
   
    if (s==0) {
        
            $("#slideop").slideDown("slow");
            s=1
        
    } 
    else {
         
            $("#slideop").slideUp("slow");
            s=0
           
    }
});
});