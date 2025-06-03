n = int(input())
a = list(map(int, input().split()))
s = [0]*(n+2)
for i in range(n, -1, -1): s[i] = s[i+1]+a[i]

def solve():
    cur = 1
    res = 0
    for i in range(n+1):
        if cur < a[i]: return -1
        res += cur
        cur -= a[i]
        if cur > s[i+1]: return -1
        cur = min(cur*2, s[i+1])
    return res

print(solve())