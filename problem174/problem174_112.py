K = int(input())

def gcd(a,b):
    if a % b == 0:
        return b
    return gcd(b, a%b)

dec = {}
for a in range(1,K+1):
    for b in range(1, K+1):
        if gcd(a,b) not in dec:
            dec[gcd(a,b)] = 1
        else:
            dec[gcd(a,b)] += 1
ans = 0
for c in range(1, K+1):
    for key in dec.keys():
        ans += gcd(c, key)*dec[key]

print(ans)
