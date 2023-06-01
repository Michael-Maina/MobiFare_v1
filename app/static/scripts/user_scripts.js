let username_container = document.querySelector(".username");
let h1 = document.querySelector('.welcome h1');
let url = window.location.href;
console.log(url)

fetch("http://localhost:5000/users/8c435eb2-3f26-4bff-ab3a-8ca33d1e07c3")
  .then((response) => response.json())
  .then((data) => {
    // Process the retrieved data
    console.log(data);
    username_container.innerHTML = `${data.first_name} ${data.last_name}`;
    h1.innerHTML = `Welcome ${data.first_name} ${data.last_name}`;
  })
  .catch((error) => {
    // Handle any errors that occurred during the request
    console.error("Error:", error);
  });


let payments_table = document.querySelector("table tbody");
let total = 0;

fetch("http://localhost:5000/users/8c435eb2-3f26-4bff-ab3a-8ca33d1e07c3/payments")
  .then((response) => response.json())
  .then((data) => {
    // Process the retrieved data
    console.log(data);
    for (const payment of data) {
      let record = document.createElement("tr");

      fetch(`http://localhost:5000/vehicles/${payment['vehicle_id']}`)
        .then((response) => response.json())
        .then((vehicleData) => {
          // Process the retrieved data
          let plate = vehicleData['number_plate'];
          let number_plate = document.createElement('td');
          number_plate.innerHTML = plate;
          record.appendChild(number_plate);

          let status = document.createElement('td');
          status.innerHTML = 'completed';
          status.classList.add('status-completed')
          record.appendChild(status);

          let date = document.createElement('td');
          date.innerHTML = payment['created_at'];
          record.appendChild(date);

          let amount = document.createElement('td');
          amount.innerHTML = `ksh. ${payment['amount']}`;
          total += payment['amount'];

          let total_container = document.querySelector('.amount_spent .figures');
          total_container.innerHTML = `ksh. ${total}`;

          record.appendChild(amount);

          payments_table.appendChild(record);
        })
        .catch((error) => {
          // Handle any errors that occurred during the request
          console.error("Error:", error);
        });
    }

  })
  .catch((error) => {
    // Handle any errors that occurred during the request
    console.error("Error:", error);
  });


