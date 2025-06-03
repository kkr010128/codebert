def i_map(): return map(int, input().split())


a, b, c, d = i_map()

ans = max(a * c, a * d, b * c, b * d)
print(ans)
