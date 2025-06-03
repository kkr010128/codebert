def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


a, b = map(int, input().split())

g = gcd(a, b)
num = g

ans = 1

for i in range(2, int(g ** 0.5) + 1):

    if num % i == 0:
        ans += 1
        while num % i == 0:
            num = num // i

if num != 1:
    ans += 1

print(ans)
