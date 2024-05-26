document.addEventListener('DOMContentLoaded', function() {
    
let  addItem = document.querySelector("#add_item");
let removeItem = document.querySelector("#remove_item");
let removeList = document.querySelector("#clear_list");
let  myList = document.querySelector(".my_list");

addItem.addEventListener("click", function(){
  let li = document.createElement("li");
  li.innerText = "Item";
   myList.appendChild(li);
});

removeItem.addEventListener("click", function(){
    let child = myList.lastElementChild;
    while (child) {
        myList.removeChild(child);
    }
});
removeList.addEventListener(("click"), function(){
    while (myList.firstChild) {
        myList.removeChild(myList.firstChild);
    }
});
})
