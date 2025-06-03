a, b, c, k = map(int, input().split())

print(max(min(k, a) ,0) - max(min(k - (a + b), c), 0))