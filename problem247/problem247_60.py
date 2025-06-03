import fractions
from functools import reduce

def lcm_base(x, y):
    return (x * y) // fractions.gcd(x, y)

def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)
    
N,M=map(int,input().split())
A=[int(i)//2 for i in input().split()]
q=lcm(*A)
#print(q)
for i in A:
    #print(i)
    if q//i%2==0:
        print(0)
        exit()
print((M//q+1)//2)