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

## Implementation
We will define a function mortgage_calculator that takes the loan amount, annual interest rate, and loan term as parameters and returns the monthly payment and total payment for the mortgage.

python

import numpy as np

def mortgage_calculator(loan_amount, annual_interest_rate, loan_term):
    n = loan_term * 12
    r = annual_interest_rate / 12
    M = loan_amount * (r * (1 + r) ** n) / ((1 + r) ** n - 1)
    total_payment = M * n
    return M, total_payment
The function mortgage_calculator takes three input parameters: loan_amount, annual_interest_rate, and loan_term. It first calculates the number of payments n by multiplying the loan term by 12. It then calculates the monthly interest rate r by dividing the annual interest rate by 12. Finally, it uses the formula to calculate the monthly payment M and the total payment by multiplying the monthly payment by the number of payments.

We can use the mortgage_calculator function to calculate the monthly payment and total payment for a mortgage. For example, to calculate the monthly payment and total payment for a mortgage with a loan amount of $200,000, an annual interest rate of 4%, and a loan term of 30 years, we can use the following code:

python

loan_amount = 200000
annual_interest_rate = 0.04
loan_term = 30
monthly_payment, total_payment = mortgage_calculator(loan_amount, annual_interest_rate, loan_term)
print("Monthly payment: ${:,.2f}".format(monthly_payment))
print("Total payment: ${:,.2f}".format(total_payment))
This will output the following result:

bash

Monthly payment: $954.83
Total payment: $343,739.28

## Conclusion
In this project, we have created a mortgage calculator using Python and the NumPy library. The calculator can be used to calculate the monthly payment and total payment for a mortgage based on the loan amount, interest rate, and loan term.

|  | Project's Name                      | Description    | GitHub's Link  |
|:--:|:--------------:|:--------------:|:--------------:|
| 1 |  -Sales-and-Operation-Sales-Project|  -             | https://github.com/IsaacSarpong/Sales-and-Operation-Sales-Project      |
| 2 |  -Shifting-Images                  |  -             | https://github.com/IsaacSarpong/Shifting-Images      |
| 3 |  -Mortgage Calculator              |  -             | https://github.com/IsaacSarpong/Mortgage-calculator     |