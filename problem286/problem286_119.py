a, b = map(int, input().split())
print(-1 if a not in range(1, 10) or b not in range(1, 10) else a*b)
