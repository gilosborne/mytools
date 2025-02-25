document.addEventListener("DOMContentLoaded", function () {
    let basePath = window.location.pathname.includes("/tools/") ? "../" : "./";

    fetch(basePath + "sidebar.html")
        .then(response => response.text())
        .then(data => {
            document.getElementById("sidebar").innerHTML = data;
        })
        .catch(error => console.error("Error loading sidebar:", error));
});
