# Sales and Operations Planning Project with Python
This project simulates a Sales and Operations Planning (S&OP) process using the zero-stock level strategy. The S&OP process aims to balance demand and supply by aligning sales forecasting, demand planning, production planning, and inventory planning. In this project, we use Python to implement a simple S&OP process that asks the user to enter initial stock, the number of months to plan, and the planned sales quantity for each month.


## Requirements
The following libraries are required to run this project:

Pandas
Matplotlib
## Project Structure
The project contains the following files:

sop.py: This is the main Python script that implements the S&OP process.
README.md: This file, which contains information about the project.
## Zero-Stock Level Strategy
The zero-stock level strategy is a simple approach to inventory management that maintains inventory levels at or near zero. Under this strategy, companies produce goods only when there is a demand for them. In other words, the inventory level is replenished only when it reaches zero.

## S&OP Process
The S&OP process implemented in this project consists of the following steps:

Data input: The user is asked to enter the initial stock, the number of months to plan, and the planned sales quantity for each month.

Data processing: The program calculates the ending stock for each month, the production quantity required to meet the demand, and the inventory level at the end of each month.

Reporting: The results of the S&OP process are reported in an easy-to-understand format, including charts and tables that show the sales forecasts, demand plans, production plans, and inventory plans.

## How to Run
To run the project, follow these steps:

Install the required libraries by running pip install pandas matplotlib.

Clone the repository to your local machine.

Navigate to the project folder.

Run python sop.py to execute the S&OP process.

Enter the initial stock, the number of months to plan, and the planned sales quantity for each month as prompted.