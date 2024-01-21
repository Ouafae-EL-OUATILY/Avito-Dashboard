const allSideMenu = document.querySelectorAll('#sidebar .side-menu.top li a');

allSideMenu.forEach(item=> {
	const li = item.parentElement;

	item.addEventListener('click', function () {
		allSideMenu.forEach(i=> {
			i.parentElement.classList.remove('active');
		})
		li.classList.add('active');
	})
});



// TOGGLE SIDEBAR
const menuBar = document.querySelector('#content nav .bx.bx-menu');
const sidebar = document.getElementById('sidebar');

menuBar.addEventListener('click', function () {
	sidebar.classList.toggle('hide');
})



const searchButton = document.querySelector('#content nav form .form-input button');
const searchButtonIcon = document.querySelector('#content nav form .form-input button .bx');
const searchForm = document.querySelector('#content nav form');

searchButton.addEventListener('click', function (e) {
	if(window.innerWidth < 576) {
		e.preventDefault();
		searchForm.classList.toggle('show');
		if(searchForm.classList.contains('show')) {
			searchButtonIcon.classList.replace('bx-search', 'bx-x');
		} else {
			searchButtonIcon.classList.replace('bx-x', 'bx-search');
		}
	}
})





if(window.innerWidth < 768) {
	sidebar.classList.add('hide');
} else if(window.innerWidth > 576) {
	searchButtonIcon.classList.replace('bx-x', 'bx-search');
	searchForm.classList.remove('show');
}


window.addEventListener('resize', function () {
	if(this.innerWidth > 576) {
		searchButtonIcon.classList.replace('bx-x', 'bx-search');
		searchForm.classList.remove('show');
	}
})



const switchMode = document.getElementById('switch-mode');

switchMode.addEventListener('change', function () {
	if(this.checked) {
		document.body.classList.add('dark');
	} else {
		document.body.classList.remove('dark');
	}
})
function generateRandomColors(count) {
   const colors = [];
   for (let i = 0; i < count; i++) {
     const color = `rgba(${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)}, 0.7)`;
     colors.push(color);
   }
   return colors;
 }
 

 document.addEventListener("DOMContentLoaded", function () {

  // Function to process data and initialize the chart
  function fetchDataAndInitializeChart(apiEndpoint, chartId, dataProcessor) {
    fetch(apiEndpoint)
      .then((response) => response.json())
      
      .then((data) => {
        
        // Process data using the provided dataProcessor function
        const chartData = dataProcessor(data);

        // Get the canvas element for the chart
        const ctx = document.getElementById(chartId).getContext("2d");

        // Create a chart based on the type specified in the chartData
        let chart;
        switch (chartData.type) {
          case "bar":
            chart = new Chart(ctx, {
              type: "bar",
              data: {
                labels: chartData.labels,
                datasets: [
                  {
                    label: chartData.datasetLabel || "Count",
                    data: chartData.data,
                    backgroundColor: chartData.backgroundColor || "rgba(75, 192, 192, 0.2)",
                    borderColor: chartData.borderColor || "rgba(75, 192, 192, 1)",
                    borderWidth: chartData.borderWidth || 1,
                  },
                ],
              },
              options: chartData.options || {
                scales: {
                  y: {
                    beginAtZero: true,
                  },
                },
              },
            });
            break;
            case "pie":
            chart = new Chart(ctx, {
              type: "pie",
              data: {
                labels: chartData.labels,
                datasets: [
                  {
                    data: chartData.data,
                    backgroundColor: chartData.backgroundColor,
                  },
                ],
              },
            });
            break;
          case "area":
            chart = new Chart(ctx, {
              type: "line",
              data: {
                labels: chartData.labels,
                datasets: [
                  {
                    label: chartData.datasetLabel || "Area",
                    data: chartData.data,
                    fill: true,
                    backgroundColor: chartData.backgroundColor || "rgba(75, 192, 192, 0.2)",
                    borderColor: chartData.borderColor || "rgba(75, 192, 192, 1)",
                    borderWidth: chartData.borderWidth || 1,
                  },
                ],
              },
              options: chartData.options || {
                scales: {
                  y: {
                    beginAtZero: true,
                  },
                },
              },
            });
            break;
          case "scatter":
            chart = new Chart(ctx, {
              type: "scatter",
              data: {
                labels: chartData.labels,
                datasets: [
                  {
                    label: chartData.datasetLabel || "Scatter",
                    data: chartData.data.map((value, index) => ({ x: index, y: value })),
                    backgroundColor: chartData.backgroundColor || "rgba(75, 192, 192, 0.2)",
                    borderColor: chartData.borderColor || "rgba(75, 192, 192, 1)",
                    borderWidth: chartData.borderWidth || 1,
                  },
                ],
              },
              options: chartData.options || {
                scales: {
                  y: {
                    beginAtZero: true,
                  },
                },
              },
            });
            break;        
          default:
            console.error(`Unsupported chart type: ${chartData.type}`);
        }
      })
      .catch((error) => console.error(`Error fetching data for ${chartId}:`, error));
  }
  

  // Define data processors for each visualization
  const dataProcessors = {
    
    myChart1: (data) => ({
      type: "bar",
      labels: data.map((item) => item.category),
      data: data.map((item) => item.count),
      backgroundColor: generateRandomColors(data.length), 
    }),
    myChart2: (data) => ({
      type: "bar",
      labels: data.map((item) => item.category),
      data: data.map((item) => item.count),
      backgroundColor: generateRandomColors(data.length), 
  }),  
    myChart3: (data) => ({
      type: "scatter",
      labels: data.map((item) => item.region),
      data: data.map((item) => item.count),
      backgroundColor: generateRandomColors(data.length), 
    }),
    myChart4: (data) => {
      const backgroundColors = generateRandomColors(data.length);
    
      return {
        type: "area", 
        labels: data.map((item) => item.city),
        data: data.map((item) => item.count),
        backgroundColor: backgroundColors,
        datasetLabel: "Count per City", 
      };
    },
    
    
    myChart5: (data) => ({
     type: "bar",
     labels: [data[0]._id], 
     data: [data[0].price], 
     datasetLabel: "Price",
     backgroundColor: "rgba(75, 192, 192, 0.2)", 
     borderColor: "rgba(75, 192, 192, 1)", 
     borderWidth: 1,
     options: {
       scales: {
         y: {
           beginAtZero: true,
         },
       },
     },
   }), 
   myChart6: (data) => {
     const uniqueCategories = [...new Set(data.map((item) => item.Product_Category))];
     const backgroundColors = generateRandomColors(uniqueCategories.length);
   
     return {
       type: "pie",
       labels: uniqueCategories,
       data: uniqueCategories.map((category) => {
         const totalCategoryPrice = data
           .filter((item) => item.Product_Category === category)
           .reduce((sum, item) => sum + item.price, 0);
         return totalCategoryPrice;
       }),
       backgroundColor: backgroundColors,
     };
   }, 

  myChart8: (data) => {
    const uniqueProducts = [...new Set(data.map((item) => item.Product_name))];
    const backgroundColors = generateRandomColors(uniqueProducts.length);
  
    return {
      type: "scatter",
      labels: uniqueProducts,
      backgroundColor: generateRandomColors(data.length), 
      data: uniqueProducts.map((product) => {
        const totalPriceForProduct = data
          .filter((item) => item.Product_name === product)
          .reduce((sum, item) => sum + item.price, 0);
        return totalPriceForProduct;
      }),
      backgroundColor: backgroundColors,
      datasetLabel: "Total Price per Product",
    };
  },
  myChart10: (data) => {
    const uniqueCategories = [...new Set(data.map((item) => item.Product_Category))];
    const backgroundColors = generateRandomColors(uniqueCategories.length);
  
    return {
      type: "area",
      labels: uniqueCategories,
      data: uniqueCategories.map((category) => {
        const totalPriceForCategory = data
          .filter((item) => item.Product_Category === category)
          .reduce((sum, item) => sum + item.price, 0);
        return totalPriceForCategory;
      }),
      backgroundColor: backgroundColors,
      datasetLabel: "Total Price per Category",
    };
  },   

  }; 
  fetch('/api/visualization18')
  .then((response) => response.json())
  .then((data) => {
      // Extract data from the API response
      const totalProducts = data[0].total_products;
      const nbrCitys = data[0].nbr_citys;
      const nbrCategorys = data[0].nbr_categorys;

      // Display the data on your webpage as needed
      document.getElementById('total_products').innerText = `Announcements ${totalProducts}`;
      document.getElementById('nbr_citys').innerText = `Active cities ${nbrCitys}`;
      document.getElementById('nbr_categorys').innerText = `Categories ${nbrCategorys}`;
  })
  .catch((error) => console.error('Error fetching data:', error));


 
  // Fetch and initialize charts for each visualization
  for (const [chartId, dataProcessor] of Object.entries(dataProcessors)) {
    const apiEndpoint = `http://127.0.0.1:5000/api/${chartId.replace("myChart", "visualization")}`;
    fetchDataAndInitializeChart(apiEndpoint, chartId, dataProcessor);
  }
});


 