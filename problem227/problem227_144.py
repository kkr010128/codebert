N, K = [int(s) for s in input().split()]
H = sorted([int(s) for s in input().split()])[::-1]
print(sum(H[K:]) if N > K else 0)