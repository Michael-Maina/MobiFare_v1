vehiclesLi.addEventListener("click", fill_vehicles);

function fill_vehicles() {
  fetch(`https://mobifare.tech/api/owners/${owner_id}/vehicles`)
    .then((response) => response.json())
    .then((data) => {
      const tableBody = document.querySelector(".vehicles_table tbody");

    //   if (tableBody.rows.length > 1) {
    //     // Check if there are rows other than the header row
    //     var rowCount = tableBody.rows.length;
    //     for (var i = rowCount - 1; i > 0; i--) {
    //       // Start from the last row (excluding the header row)
    //       tableBody.deleteRow(i);
    //     }
    //   }
      console.log(data);
      data.forEach((vehicle) => {
        const row = document.createElement("tr");

        // Create and populate the cells
        const numberPlateCell = document.createElement("td");
        numberPlateCell.textContent = vehicle.number_plate;
        row.appendChild(numberPlateCell);

        const idCell = document.createElement("td");
        idCell.textContent = vehicle.id;
        row.appendChild(idCell);

        const createdAtCell = document.createElement("td");
        createdAtCell.textContent = vehicle.created_at;
        row.appendChild(createdAtCell);

        const deleteCell = document.createElement("td");
        const deleteButton = document.createElement("button");
        deleteButton.classList.add("delete_button");
        deleteButton.textContent = "Delete";
        deleteButton.onclick = () => deleteRow(vehicle.id); // Assuming there's a deleteRow function
        deleteCell.appendChild(deleteButton);
        row.appendChild(deleteCell);

        tableBody.append(row);
      });
    })
    .catch((error) => {
      // Handle any errors
      console.error("Error:", error);
    });
}

function deleteRow(vehicle_id) {
  fetch(`https://mobifare.tech/api/vehicles/${vehicle_id}`, {
    method: "DELETE",
  })
    .then((response) => {
      console.log(response);
      return response.json();
    })
    .then((data) => {
      console.log(data);
    })
    .catch((error) => {
      // Handle any errors
      console.error("Error:", error);
    });
}
