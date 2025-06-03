string = input()

lt = True
ans = 0
l_cnt = 0
m_cnt = 0
if string[0] == ">":
    lt = False

for s in string:
    if s == "<":
        if not lt:
            a, b = max(l_cnt, m_cnt), min(l_cnt, m_cnt)
            ans += a * (a + 1) // 2 + b * (b - 1) // 2
            l_cnt = m_cnt = 0
        l_cnt += 1
        lt = True
    else:
        m_cnt += 1
        lt = False
a, b = max(l_cnt, m_cnt), min(l_cnt, m_cnt)
ans += a * (a + 1) // 2 + b * (b - 1) // 2
print(ans)