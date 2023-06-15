var barColors = [
  "#00aba9",
  "#2b5797",
  "#b91d47",
  "#472183",
  "#27374D",
  "#116A7B",
];

let url = window.location.href;
let id = url.split("/").pop();
let h1 = document.querySelector(".welcome h1");
let username_container = document.querySelector(".username");
const sumArray = (array) => array.reduce((total, num) => total + num, 0);

fetch(`https://mobifare.tech/api/owners/${id}`)
  .then((response) => response.json())
  .then((data) => {
    username_container.innerHTML = `${data.first_name} ${data.last_name}`;
    h1.innerHTML = `Welcome ${data.first_name} ${data.last_name}!`;
  })
  .catch((error) => {
    console.error(error);
  });

function renderNoPaymentsText(statement) {
  const canvas = document.getElementById("barChart");
  const piechart = document.getElementById("myChart");

  const context = canvas.getContext("2d");
  const piecontext = piechart.getContext("2d");

  const text = statement;
  const x = canvas.width / 2;
  const y = canvas.height / 2;
  const piex = piechart.width / 2;
  const piey = piechart.height / 2;

  context.font = piecontext.font = "12px Arial";
  context.textAlign = piecontext.textAlign = "center";
  context.textBaseline = piecontext.textBaseline = "middle";

  context.fillText(text, x, y);
  piecontext.fillText(text, piex, piey);
}

let vehicle_dict = {};
fetch(`https://mobifare.tech/api/owners/${id}/vehicles`)
  .then((response) => response.json())
  .then((vehicles) => {
    console.log(vehicles);
    if (vehicles.length == 0) {
      renderNoPaymentsText("No vehicles registered");
    }
    let dataset = [];
    let xValues = [];
    let hasPayments = false;
    for (const vehicle of vehicles) {
      let dict = {};
      let vehicle_id = vehicle["id"];
      i = 0;
      if (vehicle_id) {
        fetch(`https://mobifare.tech/api/vehicles/${vehicle_id}/payments`)
          .then((response) => response.json())
          .then((payments) => {
            if (payments.length > 0) {
              hasPayments = true;
            }

            let set = {};

            for (const payment of payments) {
              if (payment.status == "completed") {
                console.log(payment);
                let record = document.createElement("tr");

                let plate = payment.number_plate;
                let number_plate = document.createElement("td");
                number_plate.innerHTML = plate;
                record.appendChild(number_plate);

                let curr_status = payment.status;
                let status = document.createElement("td");
                status.innerHTML = curr_status;
                if (curr_status == "pending") {
                  status.classList.add("status-pending");
                } else if (curr_status == "completed") {
                  status.classList.add("status-completed");
                } else if (curr_status == "cancelled") {
                  status.classList.add("status-cancelled");
                }
                record.appendChild(status);

                let date = document.createElement("td");
                date.innerHTML = payment["created_at"];
                record.appendChild(date);

                let amount = document.createElement("td");
                amount.innerHTML = `ksh. ${payment["amount"]}`;
                record.appendChild(amount);

                document
                  .querySelector(".payment_record table")
                  .appendChild(record);

                let month = payment["created_at"].split(" ")[2];
                if (xValues.includes(month) == false) {
                  xValues.push(month);
                }
                if (dict.hasOwnProperty(month)) {
                  dict[month] += payment["amount"];
                } else {
                  dict[month] = payment["amount"];
                }
              }
            }

            set["label"] = vehicle["number_plate"];

            let vehicle_data = Object.values(dict);
            // console.log(vehicle_data);
            if (vehicle_data.length == 0) {
              vehicle_data.push(0);
            }
            set["data"] = vehicle_data;
            // console.log(vehicle_data);
            // console.log(set);
            set["backgroundColor"] = barColors[i++];

            dataset.push(set);

            if (
              vehicles.indexOf(vehicle) === vehicles.length - 1 &&
              hasPayments
            ) {
              // Create the chart only when all vehicles' data is fetched
              console.log(dict);
              console.log("here");
              // console.log(xValues);
              // console.log(dataset);
              console.log(hasPayments);
              new Chart("barChart", {
                type: "bar",
                data: {
                  labels: xValues,
                  datasets: dataset,
                },
                options: {
                  legend: { display: false },
                  title: {
                    display: true,
                    text: "Vehicle monthly charts",
                  },
                },
              });

              let pieX = [];
              let pieY = [];
              for (const set of dataset) {
                pieX.push(set["label"]);
                pieY.push(sumArray(set["data"]));
              }

              new Chart("myChart", {
                type: "doughnut",
                data: {
                  labels: pieX,
                  datasets: [
                    {
                      backgroundColor: barColors,
                      data: pieY,
                    },
                  ],
                },
                options: {
                  title: {
                    display: true,
                    text: "Your vehicles productivity",
                  },
                },
              });
            } else {
              renderNoPaymentsText("No payments made");
            }
          })
          .catch((error) => {
            // Handle any errors that occurred during the request
            console.error("Error:", error);
          });
      }
    }
  })
  .catch((error) => {
    // Handle any errors that occurred during the request
    console.error("Error:", error);
  });
