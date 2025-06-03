a, b, c, d = map(int, input().split())
h = a * c
i = a * d
j = b * c
k = b * d
print(max(h, i, j, k))