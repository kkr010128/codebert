h_1 , m_1, h_2, m_2 , k = map(int, input().split())
# study_time = ((h_2*60 + m_2) - (h_1*60 + m_1))
study_time = ((h_2*60 + m_2) - (h_1*60 + m_1))
print(study_time - k)