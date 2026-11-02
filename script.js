
const form = document.getElementById("regForm");

const nameInput = document.getElementById("name");
const emailInput = document.getElementById("email");
const phoneInput = document.getElementById("phone");
const collegeInput = document.getElementById("college");
const eventInput = document.getElementById("event");

const error = document.getElementById("error");
const success = document.getElementById("success");
const count = document.getElementById("count");
const tableBody = document.querySelector("#regTable tbody");

let registeredCount = 0;

// Display the server name
document.getElementById("host").textContent =
    window.location.hostname || "localhost";

// Form submission
form.addEventListener("submit", function (e) {
    e.preventDefault();

    error.textContent = "";
    success.textContent = "";

    const name = nameInput.value.trim();
    const email = emailInput.value.trim();
    const phone = phoneInput.value.trim();
    const college = collegeInput.value.trim();
    const event = eventInput.value;

    // Check empty fields
    if (!name || !email || !phone || !college || !event) {
        error.textContent = "Please fill in all the fields.";
        return;
    }

    // Validate email
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (!emailPattern.test(email)) {
        error.textContent = "Please enter a valid email address.";
        return;
    }

    // Validate 10-digit mobile number
    const phonePattern = /^[0-9]{10}$/;

    if (!phonePattern.test(phone)) {
        error.textContent = "Please enter a valid 10-digit mobile number.";
        return;
    }

    // Add participant to table
    registeredCount++;

    const row = tableBody.insertRow();

    row.insertCell(0).textContent = registeredCount;
    row.insertCell(1).textContent = name;
    row.insertCell(2).textContent = event;

    count.textContent = registeredCount;

    success.textContent =
        "Registration successful! Welcome, " + name + ".";

    // Clear the form
    form.reset();
});

// Clear messages when form is reset
form.addEventListener("reset", function () {
    error.textContent = "";
    success.textContent = "";
});
