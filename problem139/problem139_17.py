h_1, m_1, h_2, m_2, k = map(int, input().split())
minute_1 = h_1*60 + m_1
minute_2 = h_2*60 + m_2
ans = minute_2 - k - minute_1
print(ans)