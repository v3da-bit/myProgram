$(document).ready(function () {
    $("#ani").click(function () { 
        $("#anime").animate({
            left:1000,
            height:200/2,
            width:200/2
        })
        $("#anime").animate({
            top:200
            
        })
        $("#anime").animate({
            
           // top:200,
            left:0,
        })
        $("#anime").animate({
            top:0, 
            height:200,
            width:200
        })
        
        
    });
$("#size").click(function () { 
    $("#anime").animate({
        height:200/2,
        width:200/2
      })
      $("#anime").animate({
         
        height:200,
        width:200
    })
  
     
    
});
});