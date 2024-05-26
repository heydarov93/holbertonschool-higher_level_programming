let head = document.querySelector("header");
let updateHeadText = document.querySelector("#update_header");
updateHeadText.addEventListener("click", function(){
  head.innerText="New Header!!!";
});