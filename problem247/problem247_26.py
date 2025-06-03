
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
harf_lcm     =lcm//2             # 最小公倍数の半分
harf_lcm_num =M//harf_lcm          # Mの中の半公倍数の個数
harf_lcm_num =(harf_lcm_num +1)//2 # 偶数を除く

#半公倍数がaiで割り切れるときは✖
import numpy as np 
A_np =np.array(A)
if np.any(harf_lcm % A_np ==0):
    harf_lcm_num =0
"""    
for a in A:
    if harf_lcm % a ==0:
        harf_lcm_num =0
        break
"""
print(harf_lcm_num)