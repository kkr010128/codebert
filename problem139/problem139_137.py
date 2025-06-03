h1, m1, h2, m2, k = [int(i) for i in input().split()]

m1 += h1 * 60
m2 += h2 * 60

m = 0
if m1 == m2:
  m = 24 * 60
elif m1 < m2:
  m = m2 - m1
else:
  m = 24 * 60 - (m1 - m2)

print(m - k)