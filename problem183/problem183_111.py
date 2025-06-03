n = int(input())

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    #divisors.sort()
    return divisors

d1 = make_divisors(n)
d2 = make_divisors(n-1)

ans = 0
for k in d1:
    if k == 1:
        continue
    temp = n
    while temp%k == 0:
        temp //= k
    if temp%k == 1:
        ans += 1
ans += len(d2)-1
print(ans)
