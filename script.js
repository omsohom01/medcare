document.getElementById("login-form").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent form from submitting

    // Get form values
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    // Error elements
    const emailError = document.getElementById("emailError");
    const passwordError = document.getElementById("passwordError");
    const loginMessage = document.getElementById("loginMessage");

    // Reset error messages
    emailError.style.display = "none";
    passwordError.style.display = "none";
    loginMessage.textContent = "";

    let valid = true;

    // Email validation
    if (!email.includes("@") || !email.includes(".")) {
        emailError.textContent = "Please enter a valid email address.";
        emailError.style.display = "block";
        valid = false;
    }

    // Password validation
    if (password.length < 6) {
        passwordError.textContent = "Password must be at least 6 characters.";
        passwordError.style.display = "block";
        valid = false;
    }

    if (valid) {
        // Mock login success (Replace this with actual login API call in a real app)
        loginMessage.textContent = "Login successful!";
        loginMessage.style.color = "green";

        // Redirect to the dashboard (Placeholder)
        setTimeout(() => {
            window.location.href = "dashboard.html"; // Replace with actual dashboard URL
        }, 1000);
    }
});
