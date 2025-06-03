N,K = list(map(int,input().split()))

snacker = set()

for i in range(K):
    dummy=input()
    for j in [int(k) for k in input().split()]:
        snacker.add(j)
print(N-len(snacker))
