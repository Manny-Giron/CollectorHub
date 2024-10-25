window.onscroll = function () {
    makeSearchBarSticky();
};

var searchBar = document.querySelector(".search-container"); // Select by class
var sticky = searchBar.offsetTop;

document.querySelector('.menu-toggle').addEventListener('click', function () {
    const navLinks = document.querySelector('.nav-links');
    navLinks.style.display = navLinks.style.display === 'flex' ? 'none' : 'flex';
});
document.addEventListener("scroll", function () {
    const searchBar = document.querySelector(".navSearch"); // Selects the first element with the class navSearch
    const scrollThreshold = 60; // Set this to the desired scroll point in pixels

    if (window.scrollY > scrollThreshold) {
        searchBar.style.display = "flex"; // Show search bar
    } else {
        searchBar.style.display = "none"; // Hide search bar
    }
});
