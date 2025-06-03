from math import gcd

N = int(input())
A = list(map(int,input().split()))

def lcm(a,b):
  return a*b//gcd(a,b)

lcm_a = 1
 
for i in A:
    lcm_a = lcm(lcm_a,i)
 
ans = 0
for i in A:
    ans += lcm_a//i

print(ans%(10**9+7))
