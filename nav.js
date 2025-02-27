document.addEventListener("DOMContentLoaded", function () {
    fetch("/nav.html")  // Absolute path works in GitHub Pages
        .then(response => response.text())
        .then(data => {
            document.getElementById("nav-container").innerHTML = data;
        })
        .catch(error => console.error("Navigation failed to load:", error));
});
