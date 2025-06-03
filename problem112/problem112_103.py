import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, K = mapint()
As = list(mapint())
mod = 10**9+7

pos = []
neg = []
for a in As:
    if a>=0:
        pos.append(a)
    else:
        neg.append(a)
pos.sort(reverse=True)
neg.sort()
ans = 1
lenp, lenn = len(pos), len(neg)
if (lenp+lenn)==K:
    for a in As:
        ans *= a
        ans %= mod
    print(ans)
elif lenn==0:
    for i in range(K):
        ans *= pos[i]
        ans %= mod
    print(ans)
elif lenp==0:
    if K%2==0:
        for i in range(K):
            ans *= neg[i]
            ans %= mod
        print(ans)
    else:
        neg = neg[::-1]
        for i in range(K):
            ans *= neg[i]
            ans %= mod
        print(ans)        
else:
    p, n = 0, 0
    while p+n+1<K:
        if p+2<=lenp and n+2<=lenn:
            if pos[p]*pos[p+1]>=neg[n]*neg[n+1]:
                ans *= pos[p]
                p += 1
            else:
                ans *= neg[n]*neg[n+1]
                n += 2
        elif n+2<=lenn:
            ans *= neg[n]*neg[n+1]
            n += 2
        else:
            ans *= pos[p]
            p += 1
        ans %= mod
    if p+n<K:
        ans *= pos[p]
        ans %= mod
    print(ans)