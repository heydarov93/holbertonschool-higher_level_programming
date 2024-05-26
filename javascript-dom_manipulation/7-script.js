const apiUrl = "https://swapi-api.hbtn.io/api/films/?format=json";

function fetchTitle(){
    fetch(apiUrl)
    .then(res=>{
        if(!res.ok){
            throw new Error("Error");
        }
       return  res.json();
    })
    .then(data => {
        let listMovies = document.querySelector("#list_movies");
          data.results.forEach(film => {
            let movie = document.createElement("li");
            movie.innerHTML = film.title;
            listMovies.appendChild(movie);
        })
   })
    .catch(error=>{
        console.log(error);
    })

}
fetchTitle();

