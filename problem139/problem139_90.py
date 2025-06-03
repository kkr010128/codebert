h1, m1, h2, m2, k = map(int, input().split())
d = (h2 - h1) * 60 + (m2 - m1)
print(max(d - k, 0))