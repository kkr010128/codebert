h1, m1, h2, m2, k = map(int, input().split())

if m1 <= m2:
    h = h2 - h1
    m = m2 - m1
else:
    h = h2 - h1 - 1
    m = m2 - m1 + 60

m += 60 * h

print(m - k)
