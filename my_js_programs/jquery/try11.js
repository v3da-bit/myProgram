$(document).ready(function () {
    $("#submit").click(function () { 
        
        
    //Minimum eight characters, at least one letter and one number
    
    r=/^(?=.*[A-Z][a-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,15}$/
    b=document.getElementById("user").value
    a=document.getElementById("pass").value
    if (b=="") {
        document.getElementById("react").innerHTML="username must be filled"
    }
    if (r.test(a)) {
        console.log("okay")
        document.getElementById("react").innerHTML="pass and user is okay"
        
    }
    else{
        console.log("lol")
        document.getElementById("react").innerHTML="pass or user is not"

    }
    if (document.getElementById("checkbox").checked) {
        
    }
});
});