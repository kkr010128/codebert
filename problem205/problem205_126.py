from collections import defaultdict
N,p = map(int,input().split())
S = input()
S = S[::-1]
d = defaultdict(lambda:0)
r = 0
for i in range(N):
    r += int(S[i])*pow(10,i,p)
    r %= p
    d[r] += 1

ans = 0
for r in d:
    ans += d[r]*(d[r]-1)//2
ans += d[0]

if p==2 or p==5:
    S = S[::-1]
    ans = 0
    for i in range(N):
        if int(S[i])%p==0:
            ans += i+1

print(ans)