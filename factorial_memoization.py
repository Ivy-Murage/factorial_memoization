def factorial_memoization(n, memo={}):
    """Return the factorial of n using memoization."""
    # check if n is memo
    if n in memo:
        return memo[n]
    # base case
    if n < 2:
        result = 1
    elif n >= 1000000:
        result = 0
    
    else:
        # recursive case
        result = factorial_memoization(n - 1) * n
    
    memo[n] = result
    return result

# Test the program on n such that 4 <= n < 1,000,000
for n in range(4, 10):
    result = factorial_memoization(n)
    print(f"Factorial of {n} is {result}")
