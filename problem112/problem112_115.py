import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))
MOD = 10**9+7
p, n = [], []

for Ai in A:
    if Ai>=0:
        p.append(Ai)
    else:
        n.append(Ai)

if len(n)==N and K%2==1:
    n.sort(reverse=True)
    ans = 1
    
    for ni in n[:K]:
        ans *= ni
        ans %= MOD
    
    print(ans)
    exit()

if K==N and len(n)%2==1:
    ans = 1
    
    for Ai in A:
        ans *= Ai
        ans %= MOD
    
    print(ans)
    exit()

p.sort(reverse=True)
n.sort()
l = []

if K%2==1:
    ans = p[0]
    p = p[1:]
else:
    ans = 1
    
for i in range(len(p)//2):
    l.append(p[2*i]*p[2*i+1])
    
for i in range(len(n)//2):
    l.append(n[2*i]*n[2*i+1])
    
l.sort(reverse=True)
    
for li in l[:K//2]:
    ans *= li
    ans %= MOD
    
print(ans)
