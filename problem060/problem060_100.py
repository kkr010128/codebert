import sys
n,m,l=map(int,input().split())
e=[list(map(int,e.split()))for e in sys.stdin]
for c in e[:n]:print(*[sum(s*t for s,t in zip(c,l))for l in zip(*e[n:])])
