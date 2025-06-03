h1, m1, h2, m2, k = map(int, input().split())

h = h2 - h1
m = m2 - m1
m += 60 * h

print(m - k)
