h, m, h2, m2, k = map(int, input().split())
ans = (h2 * 60 + m2) - (h * 60 + m) - k
print(ans)