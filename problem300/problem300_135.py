a,b = map(int,input().split())
def gcd(x,y):
    if y == 0:
        return x
    return gcd(y,x%y)

n = gcd(a,b)
ans = 0
i = 2
while i*i <= n:
    if n%i == 0:
        while n%i == 0:
            n /= i
        ans += 1
    i += 1
if n != 1:
    ans += 1
print(ans+1)
