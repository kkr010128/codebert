n, k = map(int, input().split())
a = list(map(int, input().split()))

def f(m):
    res = sum([-(-x//m)-1 for x in a])
    return res <= k

l, r = 0, 10**9+10

while r-l > 1:
    x = (l+r)//2
    if f(x): r = x
    else: l = x

print(r)
