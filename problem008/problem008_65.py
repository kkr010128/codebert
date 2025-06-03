# 24
# ALDS_11_B - 深さ優先探索

from collections import deque

n = int(input())
u_l = []
k_l = []
v_l = []
for i in range(n):
    _in = input()
    _v_l = []
    for j,_ in enumerate(_in.split()):
        if j == 0:
            u_l.append(int(_))
        elif j == 1:
            k_l.append(int(_))
        else:
            _v_l.append(int(_))
    v_l.append(_v_l)

def dfs(v):
    global count
    c_l[v] = True
    d_l[v] = count
    count += 1
    for i in range(k_l[v]):
        _v = v_l[v][i]-1
        if not c_l[_v]:
            dfs(_v)
    f_l[v] = count
    count += 1

d_l = [None]*n
f_l = [None]*n
c_l = [False]*n
count = 1
while False in c_l:
    dfs(c_l.index(False))

for idx, d, f in zip(list(range(1,n+1)), d_l, f_l):
    print(idx, d, f)
