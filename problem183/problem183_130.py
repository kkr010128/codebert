def divisors(N):
    U = int(N ** 0.5) + 1
    L = [i for i in range(1, U) if N % i == 0]
    return L + [N // i for i in reversed(L) if N != i * i]

def solve(k):
    n = N
    while n % k == 0:
        n //= k
    return (n % k == 1)

N = int(input())

K = set(divisors(N) + divisors(N - 1)) - {1}
print(sum(solve(k) for k in K))