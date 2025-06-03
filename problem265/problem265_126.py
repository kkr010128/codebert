import math

n = int(input())
ans = math.ceil(n/1.08) 
if n != math.floor(ans*1.08):
    print(r':(')
else:
    print(ans)

