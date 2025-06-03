def gcd(a,b):
    if not b: return a
    return gcd(b,a%b)

def lcm(a, b):
    return (a*b)//gcd(a, b)

N = int(input())
A = list(map(int,input().split()))
l = 1
ans, mod = 0, 1000000007

for x in A:
    l = lcm(l, x)

for x in A:
    ans = ans + l//x
print(ans % mod)
