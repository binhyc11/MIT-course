## define user's inputs
annual_salary = float ( input ('The starting annual salary: '))
portion_saved = float (input ('The portion of salary to be saved, in decimal percentage: '))
total_cost = float ( input ('The cost of your dream home: '))
semi_annual_raise = float (input('Semi-annual salary raise, in decimal percentage: '))
r = 0.04 # annual return

time = 0 # number of months to be afford to down payment

monthly_savings = annual_salary / 12 * portion_saved
down_payment = total_cost * 0.25
current_savings = 0.0 # starting savings after the 1st month


while down_payment > current_savings:
    time += 1
    if (time - 1 ) % 6 == 0 and time != 1: # time for salary raise
        monthly_savings = monthly_savings * (1 + semi_annual_raise)
    current_savings += monthly_savings + current_savings * r/12
if down_payment <= current_savings:
    print (time)