document
  .getElementById("registerForm")
  .addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent the form from submitting the default way
    // Gather form data
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    // Create a data object
    const data = {
      username: username,
      password: password,
    };

    // Make the API call to register the user
    fetch("http://127.0.0.1:5000/api/register", {
      // Replace with your actual API endpoint
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.json();
      })
      .then((data) => {
        // Handle the response data
        if (data.success) {
          alert("Registration successful! Please log in.");
          window.location.href = "/login"; // Redirect to the login page
        } else {
          alert(`Error: ${data.message}`);
        }
      })
      .catch((error) => {
        console.error("There was a problem with the fetch operation:", error);
        alert("An error occurred. Please try again later.");
      });
  });
