document.addEventListener('DOMContentLoaded', function() {
    document.querySelector("#btn_translate").addEventListener("click", function() {
        const languageCode = document.querySelector("#language_code").value;
        const url = `https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`;
        
        fetch(url)
            .then(response => response.json())
            .then(data => {
                document.querySelector("#hello").innerText = data.hello;
            })
            .catch(error => {
                console.error('Error:', error);
                document.querySelector("#hello").innerText = "Error fetching translation";
            });
    });
});


