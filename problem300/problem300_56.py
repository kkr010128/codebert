from math import gcd
from copy import copy
a, b = map(int, input().split())

def div(x):
    ret = []
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            ret.append(i)
            ret.append(x // i)
    
    return ret

def judge_prime(x):
    cnt = 0
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            cnt += 1
        if cnt >= 2:
            return False
    return True

div_a = div(a)
div_b = div(b)

data = list(set(div_a) & set(div_b))

ans = 0
for x in data:
    if judge_prime(x):
        ans += 1
print(ans)