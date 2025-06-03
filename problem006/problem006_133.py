n=input()
m = 100000

for _ in xrange(n):
    m = m + m*0.05
    if m % 1000:
        m = m + 1000 - m % 1000
print int(m)