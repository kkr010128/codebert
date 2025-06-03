a, b, m = map(int, input().split())
a_s = list(map(int, input().split()))
b_s = list(map(int, input().split()))
m_s =[]

for _ in range(m):
    m_s.append(list(map(int, input().split())))

mini = min(a_s) + min(b_s)

for am, bm, sale in m_s:
    mini = min(mini, a_s[am-1]+b_s[bm-1]-sale)

print(mini)