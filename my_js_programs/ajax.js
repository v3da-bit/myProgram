function get(){
    //document.write("hello");
const xhr=new XMLHttpRequest();
const xhr1=new XMLHttpRequest();

    xhr.open('GET','http://dummy.restapiexample.com/api/v1/employees',true);
xhr.onprogress=function (){
    xhr1.open('GET','onprogress.html',true);
    xhr1.onload = function(){
        document.write(this.responseText);
    }
    xhr1.send();
     
}
   
    xhr.onload = function(){
        delete(xhr1);
   

        document.write(this.responseText);
    }
    xhr.send();
}