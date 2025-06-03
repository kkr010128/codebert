N = int(input())

memo = []

memo = [1,1] + [0] * (N - 1)

def f(n):
    if memo[n] == 0:
        memo[n] = f(n-1) + f(n-2)
        return(memo[n])
    if memo[n] != 0:
        return(memo[n])

print(f(N))
