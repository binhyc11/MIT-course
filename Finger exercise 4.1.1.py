# Write a function isIn that accepts two strings as arguments and
# returns True if either string occurs anywhere in the other, and False otherwise.
# Hint: you might want to use the built-in str operation in.

def isIn (x, y):
    if x in y or y in x:
        return True
    else:
        return False
    
x = input ('Enter a string: ')
y = input ('Enter a string: ')
z = isIn (x, y)
print (z)