epsilon = 0.01
k = 100


guess = k/2.0
num_guesses = 0

while abs(guess*guess - k) >= epsilon:
    guess = guess - (((guess**2) - k)/(2*guess))
    num_guesses += 1
print('Square root of', k, 'is about', guess)
print (num_guesses)