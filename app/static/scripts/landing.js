// Nav bar section
var header_content = document.querySelectorAll("nav .nav-links li a");
header_content.forEach(function (link) {
  link.classList.remove("blue-link");
  link.classList.add("white-link");
});

var logo_content = document.querySelector("nav .logo a");
logo_content.classList.remove("blue-link");
logo_content.classList.add("white-link");

var login = document.querySelector("#login");
login.classList.remove("blue-link");
login.classList.add("white-link");

document.addEventListener("scroll", function () {
  var header = document.querySelector("header");
  var scrollTop = window.pageYOffset || document.documentElement.scrollTop;

  if (scrollTop > 0) {
    header.classList.add("white");
    header_content.forEach(function (link) {
      link.classList.add("blue-link");
      link.classList.remove(".white-link");
    });

    login.classList.add("blue-link");
    login.classList.remove("white-link");

    logo_content.classList.add("blue-link");
    logo_content.classList.remove("white-link");

    header.classList.remove("transparent");
  } else {
    header.classList.add("transparent");
    header_content.forEach(function (link) {
      link.classList.remove("blue-link");
      link.classList.add("white-link");
    });

    login.classList.remove("blue-link");
    login.classList.add("white-link");

    logo_content.classList.remove("blue-link");
    logo_content.classList.add("white-link");

    header.classList.remove("white");
  }
});

document.getElementById("loginBtn").addEventListener("click", function () {
  document.getElementById("modal-signup").style.display = "block";
});

document
  .getElementsByClassName("close-signup")[0]
  .addEventListener("click", function () {
    document.getElementById("modal-signup").style.display = "none";
  });

let form = document.querySelector(".form-signup");

form.addEventListener("submit", (e) => {
  e.preventDefault();

  let first_name = document.querySelector("#firstname").value;
  let last_name = document.querySelector("#lastname").value;
  let email_address = document.querySelector("#email").value;
  let password = document.querySelector("#password").value;
  let user_type = document.querySelector("#logger-type").value;
  let phone_number = document.querySelector("#phonenumber").value;

  let form_data = {
    first_name: first_name,
    last_name: last_name,
    email_address: email_address,
    password: password,
    user_type: user_type,
    phone_number: phone_number,
  };

  // Make a POST request to the API endpoint
  fetch("http://localhost:5000/signup", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(form_data),
  })
    .then((response) => {
      console.log(response);
      if (response.redirected) {
        form.reset();
        window.location.href = response.url;
      }
    })
    .catch((error) => {
      // Handle any errors
      console.error("Error:", error);
    });
});

document.getElementById("login").addEventListener("click", function () {
  document.getElementById("modal-login").style.display = "block";
});

document
  .getElementsByClassName("close-login")[0]
  .addEventListener("click", function () {
    document.getElementById("modal-login").style.display = "none";
  });

let loginform = document.querySelector(".form-login");

loginform.addEventListener("submit", (e) => {
  e.preventDefault();

  let email_address = document.querySelector("#email-login").value;
  let password = document.querySelector("#password-login").value;
  let user_type = document.querySelector("#logger-type-login").value;

  let form_data = {
    email_address: email_address,
    password: password,
    user_type: user_type,
  };
  console.log(form_data);
  // Make a POST request to the API endpoint
  fetch("http://localhost:5000/login", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(form_data),
  })
    .then((response) => {
      console.log(response);
      if (response.redirected) {
        loginform.reset();
        window.location.href = response.url;
      }
    })
    .catch((error) => {
      // Handle any errors
      console.error("Error:", error);
    });
});
