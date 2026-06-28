# CS340
# CS 340 Project Two README

**Student:** Veronika Hryhorieva

## Project Overview

For this project, I built a dashboard for Grazioso Salvare using Python, MongoDB, and Dash. The goal was to create an interactive dashboard that allows users to view and filter animal rescue data from the Austin Animal Center database. The dashboard displays the data in a table, shows a pie chart of the animal breeds, and updates a map based on the animal selected in the table.

## Dashboard Features

The dashboard includes several interactive features:

* An interactive data table that displays all of the animal records from the database.
* Radio button filters that let the user switch between Reset, Water Rescue, Mountain or Wilderness Rescue, and Disaster or Individual Tracking.
* A pie chart that updates to show the breed distribution based on the selected filter.
* A map that automatically updates to show the location of the selected animal from the table.
* The Grazioso Salvare logo and my name displayed on the dashboard.

## Why I Chose These Tools

I used MongoDB because it works well with large collections of data and makes it easy to search and filter records. Since the animal records don't all have exactly the same structure, MongoDB was a good choice because it doesn't require a fixed table format like a relational database.

I used Python because it made it easy to connect to MongoDB and organize the dashboard. Dash was useful because it allowed me to build a web application without needing to learn JavaScript. It also made it simple to connect the data table, chart, and map so they update together whenever a filter changes or a different row is selected.

One part that helped keep my code organized was the CRUD Python module that I created in Project One. Instead of writing the database connection multiple times, I only had to call the methods from my CRUD class. This made my dashboard code much cleaner and easier to understand. If I ever build another project that uses the same database, I can reuse the CRUD module without having to rewrite all of the database code again.

## How to Run the Project

1. Make sure MongoDB is running.
2. Open the project in JupyterLab.
3. Verify that the Austin Animal Center data has already been imported into MongoDB.
4. Run the Project Two notebook.
5. Open the dashboard in the browser using the generated link.
6. Use the radio buttons to change rescue types, click different rows in the table, and watch the chart and map update automatically.

## Challenges

The hardest part of this project was getting all of the dashboard components to work together. At first I had several callback errors, indentation problems, and issues connecting my CRUD module to the dashboard. I also spent time making sure the filters returned the correct records and that the map updated when a different animal was selected.

Another challenge was making the dashboard look organized and easy to use. I adjusted the layout several times before I was happy with how everything fit together.

Overall, I learned a lot from this project. It helped me understand how a database, a Python backend, and an interactive dashboard can all work together in one application. It also gave me more practice troubleshooting errors and organizing my code so it is easier to maintain in the future.
