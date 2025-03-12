"use strict";

// Single-line comment
/* Multi-line comment */

/* Sorting Array */
let cities = ["Paris", "New York", "London", "Berlin", "Tokyo"];

function sortCities() {
    cities.sort().reverse();
    document.getElementById("result").innerText = "Sorted Cities: " + cities.join(", ");
}

/* FOR/IN Loop */
let laptop = { brand: "Apple", model: "MacBook Pro", year: 2023 };
for (let key in laptop) {
    console.log(key + ": " + laptop[key]);
}

/* Object Example */
let student = {
    firstname: "Alice",
    lastname: "Johnson"
};

// Dot Notation
console.log(student.firstname + " " + student.lastname);

// Bracket Notation
console.log(student["firstname"] + " " + student["lastname"]);

/* Variable Hoisting */
console.log(x); // Undefined due to hoisting
var x = 10;
console.log(x); // Outputs: 10

/* Strict Mode Example */
try {
    y = 5; // Will throw an error because 'y' is not declared
} catch (error) {
    console.log("Error: " + error.message);
}
