h1, m1, h2, m2, K = map(int, input().split())

h = h2-(h1+1)
m = m2+60-m1
m += 60*h

m -= K

print(m)
