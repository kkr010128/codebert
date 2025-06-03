n, k = map(int, input().split())
mod = 10**9 + 7

res = 0
z = n*(n+1)//2
for x in range(k, n+2):
    min_ = (x-1)*x//2
    max_ = z - (n-x)*(n+1-x)//2
    res += max_ - min_ + 1
    res %= mod

print(res)
