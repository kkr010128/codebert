x, y = map(int, input().split())
ans = max(4 - x, 0) + max(4 - y, 0)
print(ans * 10**5 if ans != 6 else 10**6)
