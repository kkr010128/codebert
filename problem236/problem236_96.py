H = int(input())
W = int(input())
N = int(input())

X = max(H, W)
print((N + X - 1) // X)
