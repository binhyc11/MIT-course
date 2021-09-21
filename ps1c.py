#################
## Given inputs ##
#################
annual_salary = int (input ("Enter starting salary: "))
semi_annual_raise = 0.07
annual_return = 0.04 
down_payment = 250000
current_savings = 0.0


#########################################
## Set the limits for bisection search ##
#########################################
num_guesses = 0
low = 0
high = 10000
portion_saved_as_interger = 0


#################################
## Set up the bisection search ##
#################################
while abs (current_savings - down_payment) >= 100:
    
    if current_savings >= down_payment:
        high = portion_saved_as_interger
    else:
        low = portion_saved_as_interger
    
    num_guesses += 1
    portion_saved_as_interger = int ((high + low) / 2)
    monthly_savings = annual_salary / 12 * portion_saved_as_interger / 10000
    
    
######################################################
## Reset current-savings for avoiding infinite loops##
######################################################
    current_savings = 0.0
    
        
############################################
## Find current_savings after 36 months ##
############################################
    for time in range (1, 37):
        if (time - 1 ) % 6 == 0 and time != 1:
            monthly_savings = monthly_savings * 1.07
        current_savings = monthly_savings + current_savings * 301/ 300


#######################                
## Print out fingings##
#######################      
    if abs(current_savings - down_payment) <= 100 :
        print ('Best portion saved should be: ', portion_saved_as_interger/10000)
        print ('Steps of bisection search: ',num_guesses)
        

##########################################################################################
## Statment for can't afford the house in 36 months even if saving every coin of salary ##
##########################################################################################
    if portion_saved_as_interger > 9999:
        print ('Steps of bisection search: ',num_guesses) 
        print ('You can not buy this house with you salary in 36 months :(')
        break