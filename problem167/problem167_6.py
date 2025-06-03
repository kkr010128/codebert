import math
def fact(n):
    ans = 1
    for i in range(2, n+1):
        ans*= i
    return ans
def comb(n, c):
    return fact(n)//(fact(n-c)*c)

r = float(input())
print("%.20f"%(2.0*math.pi*r))
