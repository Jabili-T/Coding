"use strict";

/* 1️ Add Event Listener to Display Date & Time */
document.getElementById("dateTimeBtn").addEventListener("click", function() {
    let now = new Date();
    document.getElementById("dateTimeDisplay").innerText = now;
});

/* 2️ JavaScript Validation (Text box should not be empty) */
function validateForm() {
    let input = document.getElementById("nameInput").value;
    if (input.trim() === "") {
        document.getElementById("errorMsg").innerText = "Text field cannot be empty!";
        return false; // Prevent form submission
    } else {
        document.getElementById("errorMsg").innerText = "";
        alert("Form submitted successfully!");
        return true; // Allow form submission
    }
}

/* 3️ Console.log() for Debugging */
function debugExample() {
    let x = 5;
    let y = 10;
    let sum = x + y;

    console.log("Value of x:", x);
    console.log("Value of y:", y);
    console.log("Sum of x and y:", sum);
}

/* 4️ Cookies: Set, Get, and Check */
function setCookie(name, value, days) {
    let expires = "";
    if (days) {
        let date = new Date();
        date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000);
        expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + value + expires + "; path=/";
    alert("Cookie set: " + name);
}

function getCookie(name) {
    let nameEQ = name + "=";
    let cookiesArray = document.cookie.split(";");
    for (let i = 0; i < cookiesArray.length; i++) {
        let cookie = cookiesArray[i].trim();
        if (cookie.indexOf(nameEQ) === 0) {
            document.getElementById("cookieResult").innerText = "Cookie Value: " + cookie.substring(nameEQ.length);
            return;
        }
    }
    document.getElementById("cookieResult").innerText = "No cookie found!";
}

function checkCookie() {
    let user = getCookie("user");
    if (user) {
        document.getElementById("cookieResult").innerText = "Welcome back, " + user;
    } else {
        document.getElementById("cookieResult").innerText = "No user cookie found!";
    }
}

/* 5️ JSON Object Access */
let person = {
    firstName: "ALI",
    lastName: "shetty",
    age: 25,
    city: "New York"
};

function displayJsonData() {
    document.getElementById("jsonDisplay").innerText =
        `Name: ${person.firstName} ${person.lastName}, Age: ${person.age}, City: ${person.city}`;
}
