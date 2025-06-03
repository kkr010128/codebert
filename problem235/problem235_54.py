from fractions import gcd
from functools import reduce


def lcm(x,y):
    return (x*y)//gcd(x,y)


def lcm_list(nums):
    return reduce(lcm,nums,1)

mod=10**9+7
n=int(input())
A=list(map(int,input().split()))
num=lcm_list(A)
cnt=0
for i in A:
    cnt +=num//i
print(cnt%mod)