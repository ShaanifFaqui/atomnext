document.addEventListener("DOMContentLoaded", function() {
    console.log("Atom Next AI website loaded!");
});

window.addEventListener("scroll", function() {
    document.querySelector("nav").classList.toggle("scrolled", window.scrollY > 50);
})
const text = "We Build AI Automations for Businesses";
let index = 0;
function typeEffect() {
    if (index < text.length) {
        document.getElementById("hero-title").textContent += text.charAt(index);
        index++;
        setTimeout(typeEffect, 100);
    }
}
document.addEventListener("DOMContentLoaded", typeEffect);

document.querySelector('.hamburger').addEventListener('click', function() {
    this.classList.toggle('active');
    document.querySelector('.nav-items').classList.toggle('active');
    document.body.classList.toggle('no-scroll');
});

document.addEventListener("DOMContentLoaded", function () {
    // Check if user is logged in
    let isLoggedIn = localStorage.getItem("loggedIn") === "true";
    
    const bookCallBtn = document.getElementById("bookCallBtn");
    const loginPrompt = document.getElementById("loginPrompt");

    // Handle button behavior
    bookCallBtn.addEventListener("click", function (event) {
        if (!isLoggedIn) {
            event.preventDefault(); // Stop redirection
            loginPrompt.classList.remove("hidden"); // Show login prompt
        } else {
            window.location.href = "book-call.html"; // Redirect if logged in
        }
    });
});

function loginUser() {
    localStorage.setItem("loggedIn", "true"); // Store login state
    window.location.href = "index.html"; // Redirect to homepage
}

<button onclick="loginUser()">Login</button>
localStorage.setItem("loggedIn", "true");
document.addEventListener("DOMContentLoaded", function () {
    let isLoggedIn = localStorage.getItem("loggedIn") === "true";
    const bookCallBtn = document.getElementById("bookCallBtn");

    bookCallBtn.addEventListener("click", function (event) {
        if (!isLoggedIn) {
            event.preventDefault();
            alert("Please log in before booking a call.");
            // Optionally, redirect to your login page:
            window.location.href = "login.html";
        } else {
            window.location.href = "book-a-call.html";
        }
    });
});

const hamburger = document.querySelector('.hamburger');
const navItems = document.querySelector('.nav-items');

hamburger.addEventListener('click', () => {
    navItems.classList.toggle('show');
});

