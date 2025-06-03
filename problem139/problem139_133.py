h1, m1, h2, m2, k = map(int, input().split())

a = m2 - m1
if a < 0:
    mm = (h2 - h1 - 1) * 60 + (60 + a)
else:
    mm = (h2 - h1) * 60 + a


print(0 if mm - k <= 0 else mm - k)
