N, K = list(map(int, input().split()))
H = list(map(int, input().split()))
h = list(filter(lambda x: x >= K, H))
print(len(h))
