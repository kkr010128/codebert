MOD = 10**9+7

n, k = map(int, input().split())
a = list(map(int, input().split()))
p, q = [], []
for x in a:
    if x >= 0: p.append(x)
    else: q.append(x)
lp, lq = len(p), len(q)

def sp():
    p.sort(reverse=True)
    q.sort()
    ans = p[0] if k % 2 else 1
    s = []
    for i in range(0, lq-1, 2):
        s.append(q[i]*q[i+1])
    for i in range(k % 2, lp-1, 2):
        s.append(p[i]*p[i+1])
    s.sort(reverse=True)
    for i in range(k//2):
        ans *= s[i]
        ans %= MOD
    print(ans)

def sq():
    a.sort(key=lambda x: abs(x))
    ans = 1
    for i in range(k):
        ans *= a[i]
        ans %= MOD
    print(ans)

if k % 2 and not p: sq()
elif n == k and lq % 2: sq()
else: sp()
