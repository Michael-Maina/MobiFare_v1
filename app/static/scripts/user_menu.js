// Get references to the menu items
var dashboardLi = document.querySelector(".dashboard");
var paymentLi = document.querySelector(".payment");
// var settingsLi = document.querySelector('.settings');
var updateLi = document.querySelector(".settings .update-profile");
var deleteLi = document.querySelector(".settings .delete-profile");
var helpLi = document.querySelector(".help");
var signOutLi = document.querySelector(".sign_out");

// Get references to the main content sections
var dashboardContent = document.getElementById("dashboard-content");
var updateContent = document.querySelector("#settings-content .update");
// var deleteContent = document.querySelector('#settings-content .delete');
var helpContent = document.getElementById("help-content");
var paymentContent = document.getElementById("payment-content");

// Add event listeners to menu items
dashboardLi.addEventListener("click", function () {
  hideAllContent();
  dashboardContent.classList.remove("hidden");
});

updateLi.addEventListener("click", function () {
  hideAllContent();
  updateContent.classList.remove("hidden");
});

// deleteLi.addEventListener('click', function() {
//   hideAllContent();
//   deleteContent.classList.remove('hidden');
// });

paymentLi.addEventListener("click", function () {
  hideAllContent();
  paymentContent.classList.remove("hidden");
});

helpLi.addEventListener("click", function () {
  hideAllContent();
  helpContent.classList.remove("hidden");
});

// Helper function to hide all content sections
function hideAllContent() {
  dashboardContent.classList.add("hidden");
  updateContent.classList.add("hidden");
  // deleteContent.classList.add('hidden');
  helpContent.classList.add("hidden");
  paymentContent.classList.add("hidden");
}

// Show the default content initially
hideAllContent();
dashboardContent.classList.remove("hidden");




function fillform() {
  fetch(`http://localhost:5000/users/${id}`)
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      document.querySelector(".update #first-name").value = data.first_name;
      document.querySelector(".update #last-name").value = data.last_name;
      document.querySelector(".update #phone-number").value = data.phone_number;
    })
    .catch((error) => {
      console.error(error);
    });
}

updateLi.addEventListener("click", fillform);

let update_form = document.querySelector("#settings-content .update form");

update_form.addEventListener("submit", (e) => {
  e.preventDefault();

  let first_name = document.querySelector(".update #first-name").value;
  let last_name = document.querySelector(".update #last-name").value;
  let phone_number = document.querySelector(".update #phone-number").value;

  let form_data = {
    first_name: first_name,
    last_name: last_name,
    phone_number: phone_number,
  };

  console.log(form_data);
  fetch(`http://localhost:5000/users/${id}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(form_data),
  })
    .then((response) => response.json())
    .then((data) => {
      // Handle the API response
      console.log("here");
      console.log(data);

      update_form.reset();
      fillform();
    })
    .catch((error) => {
      // Handle any errors
      console.error("Error:", error);
    });
});


signOutLi.addEventListener('click', function (){
  window.location.href = 'http://localhost:3000';
})
