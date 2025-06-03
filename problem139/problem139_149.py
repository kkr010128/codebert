h1, m1, h2, m2, k = list(map(int, input().split()))
if m2 < m1:
    while m2 < m1:
        h2 -= 1
        m2 += 60
tm = m2 - m1
th = h2 - h1
if k > (th*60 + tm):
    print (0)
else:
    print(th*60 + tm - k)