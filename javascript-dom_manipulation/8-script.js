const apiUrl = "https://hellosalut.stefanbohacek.dev/?lang=fr";

function fetchLang(){
    fetch(apiUrl)
    .then(res=>{
        if(!res.ok){
            throw new Error("Error");
        }
       return  res.json();
    })
    .then(data => {
         let text = document.querySelector("#hello");
         text.innerHTML = data.hello;
        })
  
    .catch(error=>{
        console.log(error);
    })

}
fetchLang();

