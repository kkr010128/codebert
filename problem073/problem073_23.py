from math import sqrt
N = int(input())
# Cが固定されAxBを入れ替えるときは省略したい

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

ans = 0
""" for C in range(1,N):
    ans += len(make_divisors(N-C)) """

for A in range(1,N):
    ans += (N-1)//A

print(ans)