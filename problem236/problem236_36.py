H = int(input())
W = int(input())
N = int(input())

q, mod = divmod(N, max(H, W))

print(q if mod == 0 else q + 1)
