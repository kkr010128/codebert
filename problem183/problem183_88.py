import sys
stdin = sys.stdin
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
nn = lambda: list(stdin.readline().split())
ns = lambda: stdin.readline().rstrip()

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors

n = ni()
ans = len(make_divisors(n-1))-1
ls = make_divisors(n)[1:]

for i in ls:
    nn = n
    while nn%i == 0:
        nn = nn//i
    if nn%i == 1:
        ans += 1

print(ans)