import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")
from copy import deepcopy
mod = 10**9 + 7

n, k = map(int, input().split())
a = [int(x) for x in input().split()]
a = sorted(a, key=lambda x: abs(x))[::-1]
a_plus = [int(x) for x in a if x > 0]
a_minus = [int(x) for x in a if x < 0]
a_abs = [abs(x) for x in a]

def calc(x):
    res = 1
    for i in x:
        res*=abs(i)
        res %= mod 
    return res

max_a = a[:k]
max_a_minus = []
max_a_plus = []
minus_cnt = 0

for i in max_a:
    if i == 0:
        print(0)
        sys.exit()
    if i < 0:
        minus_cnt += 1
        max_a_minus.append(i)
    else:
        max_a_plus.append(i)

if minus_cnt % 2 == 0:
    print(calc(max_a))
    sys.exit()

plus_cnt = k - minus_cnt

if len(a_minus) <= minus_cnt and len(a_plus) <= plus_cnt:
    ans = -float('inf')
elif len(a_minus) <= minus_cnt:
    if len(max_a_minus) == 0:
        ans = -float("inf")
    else:
        max_a_minus.pop()
        max_a_plus.append(a_plus[plus_cnt])
        ans = calc(max_a_plus + max_a_minus)
elif len(a_plus) <= plus_cnt:
    if len(max_a_plus) == 0:
        ans = -float("inf")
    else:
        max_a_plus.pop()
        max_a_minus.append(a_minus[minus_cnt])
        ans = calc(max_a_minus + max_a_plus)
else:
    flag1 = 1
    flag2 = 1
    if len(max_a_minus) == 0:
        ans1 = -float("inf")
        flag1 = 0
    if len(max_a_plus) == 0:
        ans2 = -float("inf")
        flag2 = 0
    if flag1:
        c1 = deepcopy(max_a_minus)
        c2 = deepcopy(max_a_plus)
        d1 = abs(c1.pop()); d2 = abs(a_plus[plus_cnt])
        c2.append(a_plus[plus_cnt])
        ans1 = calc(c1 + c2)
    if flag2:
        c3 = deepcopy(max_a_minus)
        c4 = deepcopy(max_a_plus)
        d3 = abs(c4.pop()); d4 = abs(a_minus[minus_cnt])
        c3.append(a_minus[minus_cnt])
        ans2 = calc(c3 + c4)
    if flag1 and flag2:
        ans = ans1 if d2*d3 > d1*d4 else ans2
    else:
        ans = max(ans1, ans2)

a_abs = a_abs[::-1]
ans2 = -calc(a_abs[:k])
if ans != -float("inf"):
    print(ans%mod)
else:
    print(ans2%mod)





