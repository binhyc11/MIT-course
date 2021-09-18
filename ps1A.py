## define user's inputs
annual_salary = float ( input ('The starting annual salary: '))
portion_saved = float (input ('The portion of salary to be saved: '))
total_cost = float ( input ('The cost of your dream home: '))
r = 0.04 # annual return

time = 0 # number of months to be afford to down payment

monthly_savings = annual_salary / 12 * portion_saved
down_payment = total_cost * 0.25
current_savings = 0.0 # starting savings after the 1st month


while down_payment > current_savings:
    time += 1
    current_savings += monthly_savings + current_savings * r/12
if down_payment <= current_savings:
    print (time)