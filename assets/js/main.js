// Set the copyright year
document.getElementById("copyright-year").textContent =
    new Date().getFullYear();


// Highlight the active navigation and footer links
document.addEventListener("DOMContentLoaded", function () {

    const currentPage = window.location.pathname.split("/").pop() || "index.html";

    // Main navigation
    document.querySelectorAll(".navbar-nav .nav-link").forEach(function (link) {
        const linkPage = link.getAttribute("href").split("/").pop();

        if (linkPage === currentPage) {
            link.classList.add("active");
            link.setAttribute("aria-current", "page");
        }
    });

    // Footer navigation
    document.querySelectorAll(".footer-links a").forEach(function (link) {
        const linkPage = link.getAttribute("href").split("/").pop();

        if (linkPage === currentPage) {
            link.classList.add("active");
            link.setAttribute("aria-current", "page");
        }
    });

});