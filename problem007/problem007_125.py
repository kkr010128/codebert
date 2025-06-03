memo = [1, 1]

def fib(n):
    if (n < len(memo)):
        return memo[n]

    memo.append(fib(n-1) + fib(n-2))
    return memo[n]

N = int(input())
print(fib(N))
