# 28
# ALDS_11_C - 幅優先探索

from collections import deque

n = int(input())
u_l = []
k_l = []
v_l = []

for i in range(n):
    _v_l = []
    for j, _ in enumerate(input().split()):
        if j == 0:
            u_l.append(int(_))
        elif j == 1:
            k_l.append(int(_))
        else:
            _v_l.append(int(_))
    v_l.append(_v_l)
        
d_l = [-1]*n
d_l[0] = 0
s_dq = deque([1])
while len(s_dq) > 0:
    _s = s_dq.popleft()
    _s -= 1
    for i in range(k_l[_s]):
        _v = v_l[_s][i]
        if d_l[_v-1] == -1:
            s_dq.append(_v)
            d_l[_v-1] = d_l[_s] + 1

for _id, _d in zip(range(1,n+1), d_l):
    print(_id, _d)

