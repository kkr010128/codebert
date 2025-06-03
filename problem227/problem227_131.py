N, K=input().split()
hp=input().split()
j = sorted([int(x) for x in hp])
print(sum([j[x] for x in range(int(N) - int(K))])) if int(K) < int(N) else print(0)