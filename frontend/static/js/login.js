document
  .getElementById("loginForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    fetch("http://127.0.0.1:5000/api/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        username: username,
        password: password,
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        // Handle login response
        console.log(data);
        if (data.success) {
          localStorage.setItem("loggedIn", "true");
          localStorage.setItem("username", data.username);
          localStorage.setItem("authToken", data.token);
          window.location.href = "/list"; // Redirect on success
        } else {
          alert(data.message);
        }
      })
      .catch((error) => console.error("Error:", error));
  });

window.onload = function () {
  if (localStorage.getItem("loggedIn") === "true") {
    window.location.href = "/list"; // Redirect if already logged in
  }
};
