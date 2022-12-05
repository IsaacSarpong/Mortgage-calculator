#Isaac Sarpong
#isaac.sarpong@azubiafrica.org

#Individual Project - Mortgage Calculator

#Collecting Data from User

loanAmount = input("How much is your mortgage loan principal? \n")
interestRate = input("What is the per annual interest rate on your mortgage? \n")
repaymentLength = input("How many years to repay your mortgage? \n")

#converting the string input variables to float
loanAmount = float(loanAmount)
interestRate = float(interestRate)
repaymentLength = float(repaymentLength)

#working out the interest rate to a decimal number
interestCalculation = interestRate / 100



#working out the number of payments over the course of the loan period.
numberOfPayments = repaymentLength*12

#Formula
#M = L[i(1+i)n] / [(1+i)n-1]

#   * M = Monthly Payment (what were trying to find out)
#   * L = Loan Amount (loanAmount)
#   * I = Interest Rate (for an interest rate of 5%, i = 0.05 (interestCalculation)
#   * N = Number of Payments (repaymentLength)

monthlyRepaymentCost = loanAmount *( interestCalculation * (1+interestCalculation) * numberOfPayments) / ((1+interestCalculation) * numberOfPayments - 1)


#working out the total cost of the repayment over the full term of the loan
totalCharge = (monthlyRepaymentCost * numberOfPayments) - loanAmount



#Output to the user
print("For a " + str(repaymentLength) + " year mortgage loan of " + str(loanAmount) + " at an annual interest rate of " + str(interestRate) + "%!")

print("You will pay $" + str(monthlyRepaymentCost) + " monthly ")

print("--------------------------------------------------------------------------------------------------")


print("The total amount paid will be $%.2f !" % totalCharge)

