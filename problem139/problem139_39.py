h1, m1, h2, m2, k = map(int, input().split())
if m2 >= m1:
    print((h2 - h1) * 60 + (m2 - m1) - k)
else:
    print((h2-1 - h1) * 60 + (m2 + 60 - m1) - k)