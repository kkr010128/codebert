
import math

def solve():
    a,b,h,m=map(int,input().split())
    sita=math.pi*2*((h+m/60)/12-m/60)
    c=math.sqrt(a*a+b*b-2*a*b*math.cos(sita))
    return c

print(solve())
