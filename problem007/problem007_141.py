memo = {}

def fib(n):
    key = n
    
    if key in memo:
        return memo[key]
    
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n > 1:
        memo[key] = fib(n-1) + fib(n-2)
    
    return memo[key]

n = int(input())
print(fib(n))