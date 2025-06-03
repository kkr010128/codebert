import math
def comb(x,y):
    return math.factorial(x)//(math.factorial(x-y)*math.factorial(y))
n,m = map(int,input().split())

ans1=0
ans2=0
if n > 1:
    ans1=comb(n,2)
if m > 1:
    ans2=comb(m,2)
print(ans1+ans2)