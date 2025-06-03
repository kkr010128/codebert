a,b,c,d = map(int,input().split())

A = [a,b]
B = [c,d]
INF = float("INF")
M = -INF

for i in A:
    for j in B:
        M = max(i*j,M)
print(M)