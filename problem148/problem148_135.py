A, B, C, K = [int(i) for i in input().split(' ')]
print(min(A, K) - max(K - B - A, 0))
