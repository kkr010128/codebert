x, k, d = map(int, input().split())
x = abs(x)

k_ = min(k, x // d)
k = k - k_
x = x-k_*d

if k % 2 != 0:
    x = abs(x-d)
print(x)
