import math
def fact(n):
    ans = 1
    for i in range(2, n+1):
        ans*= i
    return ans
def comb(n, c):
    return fact(n)//(fact(n-c)*c)

s,w = map(int, input().split())
if(s >w):
    print('safe')
else:
    print('unsafe')
