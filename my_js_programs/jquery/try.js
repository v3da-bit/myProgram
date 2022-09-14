$(document).ready(function () {
    var v=0
        
    $("#b1").click(function () { 
        if (v==0){    
        $("div .red").css("background-color","red");
        v=1
        /*function f2(){
            $("#b1").click(function () { 
                $(".blue").css("background-color", "blue");
                f3()
                function f3(){
                    $("#b1").click(function () { 
                         $(".red,.blue").css("background-color", "white");
                         $("#b1").click(function () {
                         f1() 
                         });   
                
                    });
                }
                
            });
        }*/
    
    }
    else if (v==1){
         
            $(".blue").css("background-color", "blue");
       v=2     
        
    }
       
    else if(v==2){ 
         
             $(".red,.blue").css("background-color", "white");
            
             v=0 
                
    
        
    }
});
});