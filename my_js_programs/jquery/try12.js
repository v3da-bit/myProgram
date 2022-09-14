
 


$("#confirm").keyup(function () { 
    

    var a=$("#pass1").val();
    var b=$("#confirm").val();
       
    if(b!=a){
        
        
            $("#show").css("display", "block");
            c=0
        }
    else{
            $("#show").css("display", "none");
            c=1
        }
        
});    
    $("#sub1").click(function () { 
        if (c==1) {
            return true;
            
        }
        else{
            return false
        }
    });