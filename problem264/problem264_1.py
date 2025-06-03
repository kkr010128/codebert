m_1, d_1 = map(int, input().split())
m_2, d_2 = map(int, input().split())

month = 12

if (m_1 % month + 1) == m_2 and d_2 == 1:
    print("1")
else:
    print("0")