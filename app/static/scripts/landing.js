document.getElementById("loginBtn").addEventListener("click", function() {
    document.getElementById("modal-signup").style.display = "block";
});

document.getElementsByClassName("close-signup")[0].addEventListener("click", function() {
    document.getElementById("modal-signup").style.display = "none";
});


let form = document.querySelector('.form-signup');

form.addEventListener('submit', (e)=>{
    e.preventDefault();

    let first_name = document.querySelector('#firstname').value;
    let last_name = document.querySelector('#lastname').value;
    let email_address = document.querySelector('#email').value;
    let password = document.querySelector('#password').value;
    let user_type = document.querySelector('#logger-type').value;
    let phone_number = document.querySelector('#phonenumber').value;

    let form_data = {
        'first_name': first_name,
        'last_name': last_name,
        'email_address': email_address,
        'password': password,
        'user_type': user_type,
        'phone_number': phone_number
    };

    // Make a POST request to the API endpoint
    fetch('http://localhost:5000/signup', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(form_data)
    })
    .then(response =>{
        console.log(response);
        if (response.redirected) {
            form.reset();
            window.location.href = response.url;
        }
    })
    .catch(error => {
        // Handle any errors
        console.error('Error:', error);
    });
});

document.getElementById("login").addEventListener("click", function() {
    document.getElementById("modal-login").style.display = "block";
});

document.getElementsByClassName("close-login")[0].addEventListener("click", function() {
    document.getElementById("modal-login").style.display = "none";
});

let loginform = document.querySelector('.form-login');

loginform.addEventListener('submit', (e)=>{
    e.preventDefault();

    let email_address = document.querySelector('#email-login').value;
    let password = document.querySelector('#password-login').value;
    let user_type = document.querySelector('#logger-type-login').value;

    let form_data = {
        'email_address': email_address,
        'password': password,
        'user_type': user_type
    };
    console.log(form_data)
    // Make a POST request to the API endpoint
    fetch('http://localhost:5000/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(form_data)
    })
    .then(response =>{
        console.log(response);
        if (response.redirected) {
            loginform.reset();
            window.location.href = response.url;
        }
    })
    .catch(error => {
        // Handle any errors
        console.error('Error:', error);
    });
});


