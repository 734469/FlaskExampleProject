new Chart(document.getElementById("bar-chart"), {
      type: 'line', /*This can cover most types of graphs*/
      data: {
        labels: labelsVar,
        datasets: [
          {
            label: "Population (millions)",
            backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
            data: dataVar,
            fill: false /*Only add if this isn't a bar*/
          }
        ]
      },
      options: {
         responsive: true,
         maintainAspectRatio: false,
        legend: { display: false },
        title: {
          display: true,
          text: 'Predicted world population (millions) in 2050'
        }
      }
      });