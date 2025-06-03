import math
a,b,h,m = map(int,input().split())
ans_cos = math.cos(math.pi*(60*h-11*m)/360)
ans = math.sqrt(a**2+b**2-2*a*b*ans_cos)
print(ans)