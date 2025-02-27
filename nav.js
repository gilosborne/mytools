document.addEventListener("DOMContentLoaded", function () {
    // Determine the correct relative path to `nav.html`
    let navPath = window.location.pathname.includes("/tools/") ? "../nav.html" : "nav.html";

    fetch(navPath)
        .then(response => response.text())
        .then(data => {
            document.getElementById("nav-container").innerHTML = data;
        });
});
