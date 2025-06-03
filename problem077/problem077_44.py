a, b, c, d = map(int, input().split())
v1 = a * c
v2 = a * d
v3 = b * c
v4 = b * d
print(max(v1, v2, v3, v4))