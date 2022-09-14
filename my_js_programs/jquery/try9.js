let count = 0;
let copyOfInterval = null;
function load(){
    copyOfInterval = setInterval(function(){
        if(count > 10) {
            clearInterval(copyOfInterval);
        }
        else {
            console.log("Hello", count);
            count++
        }
    }, 1000)
}


