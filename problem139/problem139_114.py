h1, m1, h2, m2, k = map(int, input().split())

h_dif = h2 - h1
m_dif = m2 - m1

time = 60*h_dif + m_dif
print(time - k)