# Let s be a string that contains a sequence of decimal numbers
# separated by commas, e.g., s = '1.23,2.4,3.123'.
# Write a program that prints the sum of the numbers in s.

total = ''
sum = 0
print ('Enter decima numbers separated by commas:')
s = input ('')
s += ',' 

## Adding one more comma after the last decima number of the string 
## --> the expression will detect the number before that comma

for i in s:
    if i != ',':
        total += i
    elif i == ',' or s[-1] != ',':
        sum += float (total)
        total = ''
    
print (sum)