function login() {
  // Basic email and password check
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  if (email && password) {
    // Hide login and show dashboard
    document.getElementById("login-section").classList.add("hidden");
    document.getElementById("dashboard").classList.remove("hidden");
  } else {
    alert("Please enter both email and password.");
  }
}

