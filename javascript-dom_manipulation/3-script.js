let header = document.querySelector("header");
let myToggle = document.querySelector("#toggle_header");

myToggle.addEventListener("click", function(){
    if(header.classList.contains("green")){
        header.classList.remove("green");
        header.classList.add("red");
    }else{
        header.classList.remove("red");
        header.classList.add("green");
    }
});