# When the implementation of fib in Figure 4.7 is used to compute fib(5),
# how many times does it compute the value of fib(2) on the way to computing fib(5)?

# The question is actually a Fibonacci of fib (5 - 2)

def countfib (n, m):
    """Count times of computing fib (m) when computing fib (n)
    n and m is a non-negative int and n > m"""
    
    def fib (n):
        """Return Fibonacci of n"""
        if n == 0 or n == 1:
            return 1
        else:
            return fib(n-1) + fib(n-2)
    x = n - m
    return fib (x)