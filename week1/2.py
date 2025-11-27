# Gross Pay
# Author: Tianxiang Wang
# Part 1

# Calculate the gross pay
def getGrossPay(hours_worked, hourly_pay_rate):
    return hours_worked * hourly_pay_rate

# Part 2

def getFinalIncome(gross_pay):
    tax = 0
    # income_start, income_end, tax rate
    income_tax_rates = [
        [0, 15600, 0.105],
        [15601, 53500, 0.175],
        [53501, 78100, 0.3],
        [78101, 180000, 0.33],
        [180001, None, 0.39]
    ]

    # get the total tax
    for item in income_tax_rates:
        income_start = item[0]
        income_end = item[1]
        tax_rate = item[2]
        if gross_pay > income_start:
            item_end = gross_pay if income_end == None else min(gross_pay, income_end)
            tax += (item_end - income_start) * tax_rate
        else:
            break


    return gross_pay - tax

# get the input

hours_worked = float(input("Please input your hours worked:"))
hourly_pay_rate = float(input("Please input your hourly pay rate:"))
gross_pay = getGrossPay(hours_worked, hourly_pay_rate)
final_income = getFinalIncome(gross_pay)
print(
    f"Your gross pay is {gross_pay:.2f}\n"
    f"Your final income without tax is {final_income:.2f}"
)



