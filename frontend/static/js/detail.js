document.addEventListener("DOMContentLoaded", function () {
  fetch("http://127.0.0.1:5000/api/bondinfo", {
    // Make sure the API URL is correct
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then((response) => response.json())
    .then((data) => {
      const tableBody = document.querySelector("#bondDetailsTable tbody");

      data.forEach((bond) => {
        const row = document.createElement("tr");

        row.innerHTML = `
                <td>${bond.id}</td>
                <td>${bond.policy}</td>
                <td>${bond.principal_address_full}</td>
                <td>${bond.bonding_company}</td>
                <td>${bond.obligee}</td>
                <td>${bond.amount}</td>
                <td>${bond.project_address_full}</td>
                <td>${bond.job_description}</td>
                <td>${bond.sign_date_day}/${bond.sign_date_month}/${bond.sign_date_year}</td>
                <td>${bond.authorized_representative}</td>
                <td><button onclick="generateForm(${bond.id})">Generate form</button></td>

            `;

        tableBody.appendChild(row);
      });
    })
    .catch((error) => console.error("Error fetching bond details:", error));
});

function generateForm(id) {
  fetch("http://127.0.0.1:5000/api/process", {
    // Make sure the API URL is correct
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      id: id,
      file_name: "AIA_Document_A310__Bid_formatted1.pdf",
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      // Handle login response
      if (data.success) {
        window.location.href = "/list"; // Redirect on success
      } else {
        alert(data.message);
      }
    })
    .catch((error) => console.error("Error:", error));
}

function logout_call() {
  window.localStorage.clear();
  window.location.href = "/";
}

window.onload = function () {
  if (!localStorage.getItem("loggedIn") && !localStorage.getItem("authToken")) {
    window.location.href = "/";
  }
};
