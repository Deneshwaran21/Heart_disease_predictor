// Add animation to form elements
document.querySelectorAll(".form-group input, .form-group select").forEach((element) => {
    element.addEventListener("focus", () => {
        element.style.transition = "all 0.3s ease-in-out";
        element.style.boxShadow = "0 0 10px rgba(100, 150, 255, 0.8)";
    });

    element.addEventListener("blur", () => {
        element.style.boxShadow = "none";
    });
});

// Form validation for Age field
const form = document.getElementById("predictionForm");
const ageInput = document.getElementById("age");
const ageError = document.getElementById("ageError");

form.addEventListener("submit", (e) => {
    if (ageInput.value < 1 || ageInput.value > 120) {
        ageError.textContent = "Please enter a valid age (1-120)";
        ageInput.focus();
        e.preventDefault();
    } else {
        ageError.textContent = "";
    }
});

form.addEventListener("submit", () => {
    console.log("Form submitted!");
});
