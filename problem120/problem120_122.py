N,K = map(int, input().split())
P = list(int(n) for n in input().strip().split())[:N]
P.sort()
total = 0
for i in range(K):
    total +=P[i]
print(total)