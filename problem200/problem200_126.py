A, B, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

vals = []
for _ in range(M):
    i, j, v = map(int, input().split())
    vals.append( a[i - 1] + b[j - 1] - v)

vals.append(min(a) + min(b))
print(min(vals))