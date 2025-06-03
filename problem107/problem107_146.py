import math
from copy import copy
di = {}
di[0] = 0
for i in range(1, 2*(10**5)+1):
    di[i] = 0
for i in range(1, 2*(10**5)+1):
    count = 0
    for j in range(int(math.log2(i))+4):
        if (i>>j)&1:
            count += 1
    di[i] = di[i%count] + 1
n = int(input())
x = list(input())
x.reverse()
count = 0
for i in x:
    if i =='1':
        count += 1
mod_p = count + 1
mod_m = count - 1
di_p = {}
di_m = {}
for i in range(n):
    di_p[i] = pow(2, i, mod_p)
    if mod_m >= 1:
        di_m[i] = pow(2, i, mod_m)
s_p = 0
s_m = 0
for i in range(n):
    if x[i] == '1':
        s_p += di_p[i]
        if mod_m >= 1:
            s_m += di_m[i]
    else:
        continue
for i in range(n-1, -1, -1):
    sm = copy(s_m)
    sp = copy(s_p)
    if x[i] == '1' and (mod_m == 0 or mod_m == -1):
        print(0)
    elif x[i] == '1':
        sm -= di_m[i]
        sm %= mod_m 
        print(di[sm]+1)
    else:
        sp += di_p[i]
        sp %= mod_p
        print(di[sp]+1)
