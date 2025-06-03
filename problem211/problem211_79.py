c, d = map(int, input().split())

if c < 10: print(d + 100 * (10-c))
else: print(d)