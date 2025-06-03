A, B, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = min(a) + min(b)
for _ in range(M):
    x, y, c = map(int, input().split())
    discount = a[x-1] + b[y-1] - c
    result = min(result, discount)

print(result)