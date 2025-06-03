#https://atcoder.jp/contests/abc158/tasks/abc158_c
import math
e,t = map(int,input().split())
t_s = list(range(math.ceil(t/0.1),math.ceil(t/0.1)+10))
ans = -1
for i in t_s:
    if math.floor(i*0.08) == e:
        ans = i
        break

print(ans)