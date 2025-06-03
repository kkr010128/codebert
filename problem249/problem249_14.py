a, b, k = map(int, input().split())
print(a - min(a, k), b - min(b, k - min(a, k)))