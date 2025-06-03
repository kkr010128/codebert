[N, K] = [int(i) for i in input().split()]
print(min(N%K, -N%K))