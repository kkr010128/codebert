def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)
def lcm(a, b):
    return a // gcd(a, b) * b

n = int(input())
a = list(map(int, input().split()))

l = 1
for i in a:
    l = lcm(l, i)

ans = 0
for i in a:
    ans += l // i

print(ans % 1000000007)