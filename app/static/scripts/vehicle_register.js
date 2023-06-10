let owner_url = window.location.href;
let owner_id = url.split("/").pop()

let form = document.querySelector('#register-content form');

form.addEventListener('submit', (e)=>{
    e.preventDefault();

    let number_plate = document.querySelector('#number-plate').value;
    let operator_email = document.querySelector('#operator-email').value;


    let form_data = {
        'number_plate': number_plate,
        'operator_email': operator_email
    };

    // Make a POST request to the API endpoint
    fetch(`http://localhost:5000/owners/${owner_id}/vehicles`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(form_data)
    })
    .then(response => response.json())
    .then(data => {
        // Handle the API response
        console.log("here");
        if (data.id){
            document.querySelector('#register-content form').reset();
            document.querySelector('#register-content .register-container').classList.add('hidden');
            document.querySelector('#register-content .success').classList.remove('hidden');

            setTimeout(()=>{
                document.querySelector('#register-content .register-container').classList.remove('hidden');
                document.querySelector('#register-content .success').classList.add('hidden');
            }, 2000);
        }
    })
    .catch(error => {
        // Handle any errors
        console.error('Error:', error);
    });
});
