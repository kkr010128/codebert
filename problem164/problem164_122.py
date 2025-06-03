def N():
    return int(input())
def L():
    return list(map(int,input().split()))
def NL(n):
    return [list(map(int,input().split())) for i in range(n)]
mod = pow(10,9)+7
#import numpy


a,b,c,d = L()
ta = -(-c // b)
ao = -(-a//d)
#print(ta,ao)
if ta <= ao :
    print("Yes")
else:
    print("No")