let  addItem = document.querySelector("#add_item");
let  myList = document.querySelector(".my_list");

addItem.addEventListener("click", function(){
  let li = document.createElement("li");
  li.innerText = "Item";
   myList.appendChild(li)
});