def get_hourly_pay():
    print("What is your hourly pay: ")
    pay = float(input("Enter your pay: "))
    return pay

def get_years():
    print("How many years would you like to calculate?")
    years = int(input("Enter your years: "))
    return years

def get_raise():
    print("What is your raise percentage?")
    raises = float(input("Enter percentage: "))
    return raises 

def getWeeklySave():
    print("How much will you save a week?")
    save = float(input("Enter Save: "))
    return save    

hourly_pay = get_hourly_pay()
hours = 40
percent_increment = get_raise()
current_year = 1
total_year_to_date = 0.0
current_year_pay = 0.0
year_raise = 0.0
current_hourly_pay = 0.0 
total_saved = 0

total_years = get_years()

weekly_save = getWeeklySave()


print("Years and there pay per year:")
for i in range(total_years):
    current_year = i + 1
    if i == 0:
        current_year_pay = (hourly_pay * hours) * 52
        print("Year " + str(current_year) + ": " + str(current_year_pay)) 
        print(hourly_pay)    
    else:
        year_raise = hourly_pay * percent_increment
        hourly_pay = hourly_pay + year_raise
        current_year_pay = (hourly_pay * hours) * 52
        print("Year " + str(current_year) + ": " + str(current_year_pay))
        print(hourly_pay)
    total_saved = current_year_pay + total_saved
    print("Saved: " + str(total_saved)) 


print("Total from year 1 to year 40:")

for i in range(total_years):
    current_year = i + 1

print("Total Saved at end of year:")

total_saved = 0
current_year_save = 0
current_year_save_raise = 0
print("Yearly Save:")
for i in range(total_years):
    current_year = i + 1
    if i == 0:
        year_save = weekly_save * 52
        print("Year " + str(current_year) + ": " + str(year_save))
    else:
        current_year_save_raise = weekly_save * percent_increment
        weekly_save = weekly_save + current_year_save_raise
        current_year_save = weekly_save * 52         
    total_saved = current_year_save + total_saved
    print("Total saved at " + str(current_year) + ": " + str(total_saved))
    print("Weekly Save: " + str(weekly_save))


def getInitialInvestment():
    print("What are your annual earnings?")
    earnings = float(input("Enter Here: "))
    return earnings

def getCompGrowth():
    print("What percentage will will your cash flow be?")
    growth = float(input("Enter Here: "))
    return growth

def getYearsGrowth():
    print("How many years will you grow at this rate?")
    years = int(input("Enter Here: "))
    return years

def getDiscountedRate():
    print("What is your discounted rate?")
    rate = float(input("Enter Here: "))
    return rate 

initialInvestment = getInitialInvestment()
compensationGrowth = getCompGrowth()
yearsGrowth = getYearsGrowth()
discountRate = getDiscountedRate()
year = 0
cashflow = 0
discount_total = 0
discounted_cash_flow = 0
current_year_cashflow = 0
current_discount_cashflow = 0
total_cash_flow = 0
total_discounted_cashflow = 0
newTotalInvestment = 0
firstInvestment = initialInvestment

for i in range(yearsGrowth):
    year = i + 1
    if year == 1:
        cashflow = initialInvestment * compensationGrowth
        discounted_total = cashflow / ((1 + discountRate) ** 1)
        discounted_cash_flow = cashflow - discount_total
        print("Year " + str(year)
        + " " + str(cashflow))
        print("Year " + str(year) + " Discounted Cash Flow: " + str(discounted_cash_flow))
        total_discounted_cashflow = discounted_cash_flow
        initialInvestment = initialInvestment + cashflow
        newTotalInvestment = initialInvestment
    else:
        cashflow = newTotalInvestment * compensationGrowth
        current_year_cashflow = cashflow
        discount_total = cashflow / ((1 + discountRate) ** year)
        discounted_cash_flow = cashflow - discount_total

        print("Year " + str(year) + " Cash Flow: " + str(current_year_cashflow))
        print("Year " + str(year) + " Discounted Cash Flow: " + str(discounted_cash_flow))
        print("Total Discounted CashFlow: " + str(total_discounted_cashflow))

        initialInvestment = initialInvestment + current_year_cashflow
        newTotalInvestment = initialInvestment + current_year_cashflow
        total_discounted_cashflow = total_discounted_cashflow + discounted_cash_flow
        print("New Total Investment " + str(newTotalInvestment))

npv = total_discounted_cashflow  - firstInvestment

print("Net Profit: " + str(npv))


