N, K = map(int, input().split())
heights = list(map(int, input().split()))
qualified = 0

for height in heights:
    if height >= K:
        qualified += 1

print(qualified)
