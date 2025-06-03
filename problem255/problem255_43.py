N = int(input())
K, X = input().split()

print(*[K[i] + X[i] for i in range(N)], sep="")

