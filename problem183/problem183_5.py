def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    return divisors


N = int(input())
d1 = make_divisors(N)
d2 = make_divisors(N - 1)

ans = len(d2) - 1
for n in d1:
    if n == 1:
        continue
    n2 = N
    while n2 % n == 0:
        n2 //= n
    if n2 % n == 1:
        if n not in d2:
            ans += 1

print(ans)
