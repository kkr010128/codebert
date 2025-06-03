#C
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

K = int(input())
ans = 0
for a in range(1,K+1):
    for b in range(a,K+1):
        for c in range(b,K+1):
            if a != b and b != c and a != c:
                ans += 6*gcd(gcd(a,b),c)
            elif a == b or b == c or a == c:
                if a == b and b == c:
                    ans += gcd(gcd(a,b),c)
                else:
                    ans += 3*gcd(gcd(a,b),c)
print(ans)