let username_container = document.querySelector(".username");
let h1 = document.querySelector('.welcome h1');
let url = window.location.href;
let id = url.split("/").pop()


let payments_table = document.querySelector("table tbody");
let total = 0;

fetch(`http://localhost:5000/users/${id}/payments`)
  .then((response) => response.json())
  .then((data) => {
    // Process the retrieved data
    console.log(data);
    for (const payment of data) {
      let record = document.createElement("tr");

      let plate = payment.number_plate;
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
    }

  })
  .catch((error) => {
    // Handle any errors that occurred during the request
    console.error("Error:", error);
  });


