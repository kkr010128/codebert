A, B, M = [int(_) for _ in input().split()]
a = [int(_) for _ in input().split()]
b = [int(_) for _ in input().split()]
xyc = [[int(_) for _ in input().split()] for i in range(M)]

rets = [min(a) + min(b)]

for x, y, c in xyc:
    rets += [a[x-1] + b[y-1] - c]
print(min(rets))