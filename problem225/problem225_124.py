import math
h,a = map(int,input().split())

if h % a != 0:
  ans = math.floor(h/a+1)
else:
  ans = math.floor(h/a)
print(ans)