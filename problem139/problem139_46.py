h1, m1, h2, m2, k = map(int, input().split())
s = h1 * 60 + m1
e = h2 * 60 + m2
print(e - k - s)