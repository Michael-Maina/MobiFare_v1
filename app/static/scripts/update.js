
function fillform() {
    fetch(`https://mobifare.tech/api/owners/${id}`)
    .then((response)=>{
        return response.json();
    })
    .then((data)=>{
        document.querySelector('.update #first-name').value = data.first_name;
        document.querySelector('.update #last-name').value = data.last_name;
        document.querySelector('.update #phone-number').value = data.phone_number;
        document.querySelector('.update #short-code').value = data.short_code;
    })
    .catch((error)=>{
        console.error(error);
    });
}

updateLi.addEventListener('click', fillform);

let update_form = document.querySelector('#settings-content .update form');

update_form.addEventListener('submit', (e)=>{
    e.preventDefault();

    let first_name = document.querySelector('.update #first-name').value;
    let last_name = document.querySelector('.update #last-name').value;
    let phone_number = document.querySelector('.update #phone-number').value;
    let short_code = document.querySelector('.update #short-code').value;


    let form_data = {
        'first_name': first_name,
        'last_name' : last_name,
        'phone_number': phone_number,
        'short_code': short_code
    };

    console.log(form_data);
    fetch(`https://mobifare.tech/api/owners/${id}`, {
        method: 'PUT',
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

        update_form.reset();
        fillform();
    })
    .catch(error => {
        // Handle any errors
        console.error('Error:', error);
    });

});
