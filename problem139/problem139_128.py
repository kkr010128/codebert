h1, m1, h2, m2, k = map(int, input().split())
H = h2 - h1
if m1 <= m2:
    M = m2 - m1
else:
    M = 60 - m1 + m2
    H -= 1
print(H*60 + M - k)