n = int(input())

memo = [0 for _ in range(45)]

def fib_memo(n):
    if memo[n] != 0:
        return memo[n]
    elif (n == 0) or (n == 1):
        return 1
    else:
        memo[n] = fib_memo(n-1) + fib_memo(n-2)
        return memo[n]
    
print(fib_memo(n))