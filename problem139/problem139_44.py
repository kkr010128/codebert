a, b, c, d, e = map(int, input().split())
f = (c - a) * 60
f += (d - b)
print(f - e)