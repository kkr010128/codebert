H = int(input())
W = int(input())
N = int(input())

m = max(H, W)
ans = int((N - 1) / m) + 1
print(ans)

