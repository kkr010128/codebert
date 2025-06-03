####
n = int(input())
memo = [-1]*(n+10)
def fib(i):
    if i==0 or i == 1:
        return 1
    if memo[i] != -1:
        return memo[i]
    memo[i] = fib(i-1) + fib(i-2)
    return memo[i]
print(fib(n))
