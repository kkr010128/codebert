#16D8102008K 1-D Greatest Common Divisor 柳生　葉月　Yagyu Hauzki
import math
a,b=map(int,input().split())
def f(x,y):
    while(1):
        tmp=x%y
        x=y
        y=tmp
        if tmp==0:
            gcd=x
            break
    return gcd
print(f(a,b))


