const apiUrl = "https://swapi-api.hbtn.io/api/people/5/?format=json";
function fetchData() {
    fetch(apiUrl)
    .then(response => {
        if(!response.ok){
            throw new Error("Error");
        }
        return response.json();
 })
 .then(data => {
    let displayCharacter = document.querySelector("#character");
    displayCharacter.innerHTML = data.name;

 })
 .catch(error=>{
    console.error("There was a problem to fetch data", error);
 });
}
fetchData();