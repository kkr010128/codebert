def divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            divisors.append(i)
            if i != n//i:
                divisors.append(n//i)
    return sorted(divisors)

N = int(input())

ans = len(divisors(N-1)) -1

for k in divisors(N)[1:]:
    N_ = N
    while N_ % k == 0:
        N_ = N_//k
    if N_ % k == 1:
        ans += 1

print(ans)

