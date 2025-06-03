_, _, m = map(int, input().split())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
low = min(a) + min(b)
for _ in range(m):
    x, y, c = map(int, input().split())
    low = min(low, a[x - 1] + b[y - 1] - c)
print(low)