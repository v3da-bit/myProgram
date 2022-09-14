$(document).ready(function () {
    $("#msgbox").click(function () { 
      
        
        if (document.getElementById("1").checked) {
            swal("Good job!", "You clicked the Correct button!", "success",{
                button:"noice"
            });

        }
        else if (document.getElementById("2").checked) {
            swal("Bad!", "You clicked the Incorrect button!", "error");
         
        }
        else{
            swal("Information!", "You clicked the Info button!", "info");

        }
        
      
        
    });
});