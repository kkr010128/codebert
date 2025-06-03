a, b, c, d = (int(i) for i in input().split())

print(max(a*c, b*d, a*d, b*c))
