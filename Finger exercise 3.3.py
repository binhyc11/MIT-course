# What would have to be changed to make the code in Figure 3.4
# work for finding an approximation to the cube root of both negative and positive
# numbers? (Hint: think about changing low to ensure that the answer lies within
# the region being searched.)


cube = float (input('Enter a number: '))
epsilon = 0.01
num_guesses = 0
low = 0
flag = True #sign of abs (cube) > 1

if abs (cube) < 1 and cube != 0:
    cube = 1 / cube
    flag = False
    
high = abs (cube)
guess = (high + low)/2.0

while abs(guess**3 - abs(cube)) >= epsilon :
    if guess**3 < abs (cube):
        
        low = guess
    else:
        
        high = guess
    
    guess = (high + low)/2.0
    num_guesses += 1
print('num_guesses =', num_guesses)

#just printing
if flag == False:
    if cube < 0:
        print (-1/guess, 'is close to the cube root of', 1/cube)
    else:
        print (1/guess, 'is close to the cube root of', 1/cube)
elif cube < 0:
    print(-guess, 'is close to the cube root of', cube)
else:
    print(guess, 'is close to the cube root of', cube)