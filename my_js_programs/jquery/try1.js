//document.getElementById("#p1").style.visibility='hidden';
let show=true;
function fun(){
   if (show==true) {
                
        $("#p1").css('visibility','hidden');
        show = false

      } 
      
      else{
        $("#p1").css('visibility','visible');
        show=true
    }
    console.log($("#p1").css('visibility'));
}
/*$(document).ready(function (){
    //$('#p1').visible();
    //$("#p1").hide();
        $('#b1').click(function () { 
            
            
           
   $('#p1').onclick(function () { 
    if ($("#p1").css('visibility','hidden')) {
                
    $("#p1").css('visibility','visible');
  }     
           
        
            else{
            $("#p1").css('visibility','hidden');
        } 
    });
}); 
        });
    
*/