N,K = map(int,input().split())
A = list(map(int,input().split()))
MOD = 10**9+7

if all(a>=0 for a in A):
    A.sort()
    ans = 1
    for _ in range(K):
        ans *= A.pop()
        ans %= MOD
    print(ans)
    exit()
if all(a<0 for a in A):
    A.sort(reverse=K%2==0)
    ans = 1
    for _ in range(K):
        ans *= A.pop()
        ans %= MOD
    print(ans)
    exit()
if N==K:
    ans = 1
    for a in A:
        ans *= a
        ans %= MOD
    print(ans)
    exit()

arr = []
for a in A:
    if a < 0:
        arr.append((-a,1))
    else:
        arr.append((a,0))

arr.sort()
pz = []
ng = []
for _ in range(K):
    v,s = arr.pop()
    if s:
        ng.append(v)
    else:
        pz.append(v)

if len(ng)%2 == 0:
    ans = 1
    for v in ng:
        ans *= v
        ans %= MOD
    for v in pz:
        ans *= v
        ans %= MOD
    print(ans)
    exit()

b = pz[-1] if pz else None
c = ng[-1] if ng else None
a = d = None
while arr and (a is None or d is None):
    v,s = arr.pop()
    if s:
        if a is None:
            a = v
    else:
        if d is None:
            d = v

if (a is None or b is None) and (c is None or d is None):
    assert False

ans = 1
if a is None or b is None:
    ans = d
    for v in ng[:-1]:
        ans *= v
        ans %= MOD
    for v in pz:
        ans *= v
        ans %= MOD
elif c is None or d is None:
    ans = a
    for v in ng:
        ans *= v
        ans %= MOD
    for v in pz[:-1]:
        ans *= v
        ans %= MOD
else:
    if a*c > b*d:
        ans = a
        for v in ng:
            ans *= v
            ans %= MOD
        for v in pz[:-1]:
            ans *= v
            ans %= MOD
    else:
        ans = d
        for v in ng[:-1]:
            ans *= v
            ans %= MOD
        for v in pz:
            ans *= v
            ans %= MOD
ans %= MOD
print(ans)