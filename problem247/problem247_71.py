
# 最小公倍数(mathは3.5以降) fractions
from functools import reduce
import fractions #(2020-0405  fractions→math)
def lcm_base(x, y):
    return (x * y) // fractions.gcd(x, y) # 「//」はフロートにせずにintにする
def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)
def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)

N,M = (int(x) for x in input().split())
A = list(map(int, input().split()))
lcm         =lcm_list(A)
han_lcm     =lcm//2
han_lcm_num =M//han_lcm
han_lcm_num =(han_lcm_num +1)//2 #偶数を除く

#半公倍数がA自身の中にある時は✖
if han_lcm in A:
    han_lcm_num =0
#半公倍数がaiで割り切れるときは✖
for a in A:
    if han_lcm % a ==0:
        han_lcm_num =0
print(han_lcm_num)