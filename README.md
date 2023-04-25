# Mortgage Calculator Using Python
In this project, we will create a mortgage calculator using Python. The calculator will take inputs such as the loan amount, interest rate, and loan term, and output the monthly payment and total payment for the mortgage.

## Requirements
The following libraries are required to run this project:

NumPy
You can install the library using the following command:

bash

pip install numpy

## Calculation Formula
The formula for calculating the monthly payment for a mortgage is as follows:

python

M = P * (r * (1 + r) ** n) / ((1 + r) ** n - 1)
where:

M is the monthly payment
P is the loan amount
r is the monthly interest rate (calculated by dividing the annual interest rate by 12)
n is the number of payments (calculated by multiplying the number of years by 12)