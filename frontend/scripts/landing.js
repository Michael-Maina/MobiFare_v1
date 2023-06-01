document.getElementById("loginBtn").addEventListener("click", function() {
    document.getElementById("modal").style.display = "block";
});

document.getElementsByClassName("close")[0].addEventListener("click", function() {
    document.getElementById("modal").style.display = "none";
});


let form = document.querySelector('form');

form.addEventListener('submit', (e)=>{
    e.preventDefault();

    let first_name = document.querySelector('#firstname').value;
    let last_name = document.querySelector('#lastname').value;
    let email_address = document.querySelector('#email').value;
    let password = document.querySelector('#password').value;
    let user_type = document.querySelector('#logger-type').value;

    let form_data = {
        'first_name': first_name,
        'last_name': last_name,
        'email_address': email_address,
        'password': password,
        'user_type': user_type
    };

    // Make a POST request to the API endpoint
    fetch('http://localhost:5000/users', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(form_data)
    })
    .then(response => response.json())
    .then(data => {
        // Handle the API response
        console.log(data);
    })
    .catch(error => {
        // Handle any errors
        console.error('Error:', error);
    });
});
