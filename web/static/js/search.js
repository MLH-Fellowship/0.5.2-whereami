const baseUrl = "http://localhost:8000";

(function() {
    document.getElementById("olc-form").addEventListener('submit', (e) => {
        e.preventDefault();
        console.log("User entered:", document.getElementById("olc").value)
        fetch(`${baseUrl}/lookup_olc?olc=${document.getElementById("olc").value}`)
        .then(res => res.json())
        .then(json => console.log("Returned: " + json.phrase))
        .catch(err => console.error(err));
    });

    document.getElementById("phrase-form").addEventListener('submit', (e) => {
        e.preventDefault();
        console.log("User entered:", document.getElementById("phrase").value)
        fetch(`${baseUrl}/lookup_phrase?phrase=${document.getElementById("phrase").value}`)
        .then(res => res.json())
        .then(json => console.log("Returned: " + json.olc))
        .catch(err => console.error(err))
    });
 })();
