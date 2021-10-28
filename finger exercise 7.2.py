def findAnEven(L):
    """
    Assumes L is a list of integers
    Returns the first even number in L
    Raises ValueError if L does not contain an even number
    """
    while True:
        try:
            if L[0] % 2 != 0:
                L.pop(0)
            else:
                return L.pop(0)
        except:
            raise ValueError ('L does not contain an even interger')
    
print (findAnEven([1, 7, 3, -8]))