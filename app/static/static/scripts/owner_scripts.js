// BAR GRAPH
var xValues = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"];
let vehicle_1 = [1000, 1500, 700, 720, 600, 1520];
let vehicle_2 = [1500, 2500, 1700, 3000, 2600, 2520];
var vehicle_3 = [1200, 2000, 1800, 2300, 2300, 2500];
var barColors = ["red", "green","blue","orange","brown"];

new Chart("barChart", {
  type: "bar",
  data: {
    labels: xValues,
    datasets: [{
      label: "KBD 247X",
      backgroundColor: "#b91d47",
      data: vehicle_1
    },
    {
        label: "KCF 237Y",
        backgroundColor: "#00aba9",
        data: vehicle_2
    },
    {
        label: "KDA 431M",
        backgroundColor: "#2b5797",
        data: vehicle_3
    }]
  },
  options: {
    legend: {display: true},
    title: {
      display: true,
      text: "Vechicle monthly charts"
    }
  }
});

const sumArray = (array) => array.reduce((total, num) => total + num, 0);

// PIE CHART

var xValues = ["KBD 247X", "KCF 237Y", "KDA 431M"];
var yValues = [sumArray(vehicle_1), sumArray(vehicle_2), sumArray(vehicle_3)];
var barColors = [
  "#b91d47",
  "#00aba9",
  "#2b5797",
  "#e8c3b9",
  "#1e7145"
];

new Chart("myChart", {
  type: "doughnut",
  data: {
    labels: xValues,
    datasets: [{
      backgroundColor: barColors,
      data: yValues
    }]
  },
  options: {
    title: {
      display: true,
      text: "Your vehicles productivity"
    }
  }
});

