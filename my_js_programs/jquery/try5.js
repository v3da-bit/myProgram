$(document).ready(function () {
    $("#date").datepicker({
        dateFormat:"dd-mm-yy",
        changeMonth:true,
        changeYear:true,
        maxDate:" +1y +1m ",
        minDate:new Date(2016,1,10),
        showOtherMonths:true,
    })
});