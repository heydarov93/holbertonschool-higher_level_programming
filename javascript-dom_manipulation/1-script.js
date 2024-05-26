let head = document.querySelector('header');
let changeColor = document.querySelector('#red_header');
const changeFunc=function changeColor(){
    head.style.color = '#FF0000';
}

changeColor.addEventListener("click", changeFunc)

// changeColor.addEventListener("click", function(){
//     head.style.color = '#FF0000';
// });


