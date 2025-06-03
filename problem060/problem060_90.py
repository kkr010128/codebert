n,m,l=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
b=[list(map(int,input().split())) for _ in range(m)]
[print(*x)for x in[[sum(s*t for s,t in zip(c,l))for l in zip(*b)]for c in a]]