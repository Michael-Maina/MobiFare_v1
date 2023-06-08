fetch(`http://localhost:5000/users/${id}`)
.then((response)=>{
    return response.json();
})
.then((data)=>{
    let phone_number = data.phone_number;

    phone_number = `254${phone_number.slice(1)}`;
    console.log(phone_number);

    let payment_form = document.querySelector('#payment-content form');

payment_form.addEventListener('submit', (e)=>{
    e.preventDefault();

    let number_plate = document.querySelector('#payment-content #number-plate').value;
    let amount = document.querySelector('#payment-content #amount').value;


    let form_data = {
        'phone_number': phone_number,
        'amount': parseInt(amount),
        'number_plate': number_plate,
        'user_id': id
    };

    console.log(form_data);
    fetch(`http://localhost:5000/payments`, {
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
        console.log(data);
    })
    .catch(error => {
        // Handle any errors
        console.error('Error:', error);
    });

});
})
.catch((error)=>{
    console.error(error);
});
