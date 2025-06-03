n,m,l=map(int,input().split())
e=[list(map(int,input().split()))for _ in[0]*(n+m)]
for c in e[:n]:print(*[sum(s*t for s,t in zip(c,l))for l in zip(*e[n:])])
