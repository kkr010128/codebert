x = int(input())
h_m_s_split = lambda x: [x // 3600, x % 3600 // 60, x % 3600 % 60]

h_m_s_data = h_m_s_split(x)

print(str(h_m_s_data[0]) + ':' + str(h_m_s_data[1]) + ':' + str(h_m_s_data[2]))
