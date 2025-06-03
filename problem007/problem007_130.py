N = int(input())

def solve(N):
    fib = [1]*(N+1)
    for i in range(2,N+1):
        fib[i] = fib[i-1] + fib[i-2]
    ans = fib[N]
    return ans
print(solve(N))
