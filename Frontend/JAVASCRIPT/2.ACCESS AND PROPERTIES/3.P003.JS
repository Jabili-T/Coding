"use strict";

/* 1 Disappear Button using 'this' */
function disappearButton() {
    this.style.display = "none";
}

/* 2️ Call() and Apply() Function Invocation */
const person = {
    fullName: function(city, country) {
        return this.firstName + " " + this.lastName + " from " + city + ", " + country;
    }
};

const user = { firstName: "Alice", lastName: "Johnson" };

// Using call()
function useCall() {
    let result = person.fullName.call(user, "Paris", "France");
    document.getElementById("callApplyResult").innerText = "Call Result: " + result;
}

// Using apply()
function useApply() {
    let result = person.fullName.apply(user, ["New York", "USA"]);
    document.getElementById("callApplyResult").innerText = "Apply Result: " + result;
}

// Difference between call() and apply():
// - call() passes arguments individually (arg1, arg2, ...)
// - apply() passes arguments as an array [arg1, arg2, ...]

/* 3️ Simple Counter */
let count = 0;
function incrementCounter() {
    count++;
    document.getElementById("counterValue").innerText = count;
}

/* 4️ Counter using Getter and Setter */
const counterObject = {
    _value: 0,
    get value() {
        return this._value;
    },
    set value(newVal) {
        if (newVal >= 0) this._value = newVal;
    }
};

function incrementAdvancedCounter() {
    counterObject.value++;
    document.getElementById("advancedCounterValue").innerText = counterObject.value;
}

/* 5️ Adding Properties to Existing Object using Prototype */
function Car(make, model) {
    this.make = make;
    this.model = model;
}

// Adding new property using prototype
Car.prototype.year = 2024;

function extendPrototype() {
    let myCar = new Car("Toyota", "Camry");
    document.getElementById("prototypeResult").innerText = 
        `Car: ${myCar.make} ${myCar.model}, Year: ${myCar.year}`;
}
