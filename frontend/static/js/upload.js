document
  .getElementById("uploadForm")
  .addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent default form submission

    const fileInput = document.getElementById("file");
    const formData = new FormData(); // Create FormData object

    if (fileInput.files.length > 0) {
      formData.append("file", fileInput.files[0]); // Append the file to FormData

      // Make the POST request to the Flask API
      fetch("http://127.0.0.1:5000/api/upload", {
        // Replace with the correct Flask API URL
        method: "POST",
        body: formData,
      })
        .then((response) => response.json()) // Parse the JSON response
        .then((data) => {
          // Handle the API response
          if (data.success) {
            alert("File uploaded successfully!");
          } else {
            alert("File upload failed: " + data.message);
          }
        })
        .catch((error) => console.error("Error:", error));
    } else {
      alert("Please select a PDF file to upload.");
    }
  });

window.onload = function () {
  if (!localStorage.getItem("loggedIn") && !localStorage.getItem("authToken")) {
    window.location.href = "/";
  }
};
