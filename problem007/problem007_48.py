def fibonacci(n, memo=None):
    if memo==None:
        memo = [None]*n
    if n<=1:
        return 1 
    else:
        if memo[n-2]==None:
            memo[n-2] = fibonacci(n-2, memo)
        if memo[n-1]==None:
            memo[n-1] = fibonacci(n-1, memo)
    return memo[n-1] + memo[n-2]

n = int(input())
print(fibonacci(n))