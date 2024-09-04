
document.addEventListener('DOMContentLoaded', function() {
    const toggler = document.querySelector('.navbar-toggler');
    const navMenu = document.querySelector('.navmenu');

    toggler.addEventListener('click', function() {
        navMenu.classList.toggle('active');
    });
});

function toggleSidebar() {
    var sidebar = document.getElementById("sidebar");
    if (sidebar.style.width === "250px") {
        sidebar.style.width = "0";
        sidebar.style.transition = "width 0.3s ease";
    } else {
        sidebar.style.width = "250px";
        sidebar.style.transition = "width 0.3s ease";
    }
}


