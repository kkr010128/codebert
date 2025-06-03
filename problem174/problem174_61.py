import math

k = int(input())

ab = []
ans = 0
for a in range(1,k+1):
    for b in range(1,k+1):
        if a % b == 0:
            ab.append(b)
        elif b % a == 0:
            ab.append(a)
        else:
            ab.append(math.gcd(a, b))
for i in ab:
    for c in range(1,k+1):
        if i % c == 0:
            ans += c
        elif c % i == 0:
            ans += i
        else:
            ans += math.gcd(i, c)

print(ans)