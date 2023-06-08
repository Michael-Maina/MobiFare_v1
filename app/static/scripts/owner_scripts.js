// BAR GRAPH
var xValues = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"];
let vehicle_1 = [1000, 1500, 700, 720, 600, 1520];
let vehicle_2 = [1500, 2500, 1700, 3000, 2600, 2520];
var vehicle_3 = [1200, 2000, 1800, 2300, 2300, 2500];
var barColors = ["red", "green", "blue", "orange", "brown"];

let url = window.location.href;
let id = url.split("/").pop();

let vehicle_dict = {};
let dataset = [];
fetch(`http://localhost:5000/owners/${id}/vehicles`)
  .then((response) => response.json())
  .then((data) => {
    console.log(data);
    // for (const vehicle of data) {
    //   let dict = {};
    //   let vehicle_id = vehicle["id"];
    //   if (vehicle_id) {
    //     fetch(`http://localhost:5000/vehicles/${vehicle_id}/payments`)
    //       .then((response) => response.json())
    //       .then((data) => {
    //         let set = {};
    //         // console.log(data);

    //         for (const payment of data) {
    //           let month = payment["created_at"].split(" ")[2];
    //           if (dict.hasOwnProperty(month)) {
    //             dict[month] += payment["amount"];
    //           } else {
    //             dict[month] = payment["amount"];
    //           }
    //         }
    //         set["label"] = data[0]["number_plate"];

    //         let vehicle_data = Object.values(dict);
    //         // console.log(vehicle_data);
    //         set["data"] = vehicle_data;
    //         set["backgroundColor"] = barColors;

    //         // console.log(set);
    //         dataset.push(set);
    //         console.log(dataset);

            // var xValues = Object.keys(dict);
            // new Chart("barChart", {
            //   type: "bar",
            //   data: {
            //     labels: xValues,
            //     datasets: dataset,
            //   },
            //   options: {
            //     legend: { display: true },
            //     title: {
            //       display: true,
            //       text: "Vechicle monthly charts",
            //     },
            //   },
            // });
          })
          .catch((error) => {
            // Handle any errors that occurred during the request
            console.error("Error:", error);
          });
  //     }
  //   }
  // })
  // .catch((error) => {
  //   // Handle any errors that occurred during the request
  //   console.error("Error:", error);
  // });

new Chart("barChart", {
  type: "bar",
  data: {
    labels: xValues,
    datasets: [
      {
        label: "KBD 247X",
        backgroundColor: "#b91d47",
        data: vehicle_1,
      },
      {
        label: "KCF 237Y",
        backgroundColor: "#00aba9",
        data: vehicle_2,
      },
      {
        label: "KDA 431M",
        backgroundColor: "#2b5797",
        data: vehicle_3,
      },
    ],
  },
  options: {
    legend: { display: true },
    title: {
      display: true,
      text: "Vechicle monthly charts",
    },
  },
});

const sumArray = (array) => array.reduce((total, num) => total + num, 0);

// PIE CHART

var xValues = ["KBD 247X", "KCF 237Y", "KDA 431M"];
var yValues = [sumArray(vehicle_1), sumArray(vehicle_2), sumArray(vehicle_3)];
var barColors = ["#b91d47", "#00aba9", "#2b5797", "#e8c3b9", "#1e7145"];

new Chart("myChart", {
  type: "doughnut",
  data: {
    labels: xValues,
    datasets: [
      {
        backgroundColor: barColors,
        data: yValues,
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
