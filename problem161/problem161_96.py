import math
a,b,c=map(int,input().split())
if b>c:
    print(math.floor((a*c)/b)-a*(math.floor(c/b)))
else:
    print(math.floor((a*(b-1))/b)-a*(math.floor((b-1)/b)))