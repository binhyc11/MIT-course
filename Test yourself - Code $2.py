####################
## EXAMPLE: perfect squares
####################



####################
## TEST YOURSELF!
## Modify the perfect squares example to print 
## imaginary perfect sqrts if given a negative num.
####################

ans = 0
neg_flag = False
confirm = 'yes' or 'Yes'
x = int(input("Enter an integer: "))

if x < 0:
    neg_flag = True
while ans**2 < x:
    ans = ans + 1
if ans**2 == x:
    print("Square root of", x, "is", ans)
else:
    print(x, "is not a perfect square")
    if neg_flag:
        print ("Just checking... did you mean", -x, "?")
        if input ('Yes/ no? ') == 'yes' or 'Yes':
            while ans**2 < abs (x):
                ans = ans + 1
            if ans**2 == abs (x):
                print("Then square root of", -x, "is", ans)
            else:
                print('Then', -x, "is not a perfect square")