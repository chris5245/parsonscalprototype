yearlycashflows = []
def getGrowthRate():
    print("What is your Annual Growth Rate?")
    rate = float(input("Enter Here: "))
    return rate

def getYears():
    print("How many years?")
    years = int(input("Enter Here: "))
    return years

def getDiscountRate():
    print("What is your discount rate?")
    rate = float(input("Enter Here: "))
    return rate

def getInitialInvestment():
    print("what is your investment?")
    invest = float(input("Enter Here: "))
    return invest

def getYearlyExpenses():
    print("what is your yearly expenses?")
    expenses = float(input("Enter Here: "))
    return expenses

def getYearlyIncome():
    print("what is your yearly income?")
    income = float(input("Enter Here: "))
    return income

def getExpensesGrowth():
    print("What is your expenses growth?")
    growth = float(input("Enter Here: "))
    return growth    
    
        

initialInvestment = getInitialInvestment()

discounted_cash_flow = 0
total_discounted_cashflow = 0
years = getYears()
annualGrowth = getGrowthRate()
cashflow = 0
newValue = 0
discountRate = getDiscountRate()

def cashFlowArray():
    income = getYearlyIncome()
    expenses = getYearlyExpenses()
    growth = getExpensesGrowth()
        
    for i in range(years):
        if i == 0:
            cashflow = income - expenses
            yearlycashflows.append(cashflow)
            newValue = cashflow
        else:
            newIncome = income + (income * annualGrowth)
            newExpenses = expenses + (expenses * growth)
            income = newIncome
            expenses = newExpenses 
            cashflow = income - expenses
            yearlycashflows.append(cashflow)
            newValue = newValue + cashflow

cashFlowArray()                

for i in range(len(yearlycashflows)):
    year = i + 1
    discounted_cash_flow = (yearlycashflows[i] / (1 + discountRate) ** year)
    print("Year " + str(year) + " Discounted Cashflow: " + str(discounted_cash_flow))
    total_discounted_cashflow = total_discounted_cashflow + discounted_cash_flow
    print("Total Discounted Cashflow: " + str(total_discounted_cashflow))

npv = total_discounted_cashflow - initialInvestment

print("NPV: " + str(npv))