n,k = map(int,input().split())


p = [0 for _ in range(n)]
p = [int(s) for s in input().split()]
p.sort()

sm = 0
for i in range(k):
    sm += p[i]

print(sm)
