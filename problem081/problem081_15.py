import math
a,b,c=[int(i) for i in input().split()]
e=math.ceil(a/c)
if(e<=b):
    print('Yes')
else:
    print('No')