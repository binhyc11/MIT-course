# # Write a program that asks the user to enter an integer and prints
# # two integers, root and pwr, such that 0 < pwr < 6 and root**pwr is equal to the integer
# # entered by the user. If no such pair of integers exists, it should print a message
# # to that effect
num = int (input('Enter an interger: '))
root = 0
pwr = 1

while pwr < 6:
    while root ** pwr <= abs (num):
        if root ** pwr == abs (num):
            if num == 0:
                print (root, pwr)
            elif num < 0 and pwr % 2 != 0:
                print (-root, pwr)
            elif num > 0 and pwr % 2 == 0:
                print (root, - root, pwr)
            elif num > 0 and pwr % 2 != 0:
                print (root, pwr)
        root += 1
    root = 0
    pwr +=1
 