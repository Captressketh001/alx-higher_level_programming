// js
// document.querySelector('#red_header').addEventListener('click', ($event) =>{
//     $event.preventDefault();
//     document.querySelector('header').style.color = '#FF0000'
// })

// jquery
$(function () {
    $('#red_header').click(function(){
        $('header').css('color', '#FF0000')
    })
});
