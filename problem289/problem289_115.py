from math import tan,radians
a,b,w=map(int,input().split())
V=a**2*b
def taiseki(x,a,b):
    x=90-x
    if tan(radians(x))>a/b:
        x=90-x
        return V-(a**3*tan(radians(x)))/2
    else:
        return a*b**2*tan(radians(x))/2
if V==w:
    print(0)
    exit()
ok,ng=0,90
while ng-ok>0.00000001:
    mid=(ok+ng)/2
    if taiseki(mid,a,b)>=w:
        ok=mid
    else:
        ng=mid
print(ng)