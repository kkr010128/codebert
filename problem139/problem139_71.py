h1, m1, h2, m2, k = map(int, input().split())
h_diff = 60*(h2 - h1)
m_diff = m2 - m1
print(h_diff + m_diff - k)