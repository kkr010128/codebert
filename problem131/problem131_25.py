a,v,b,w,t=map(int,open(0).read().split())
if (a<b and a+v*t>=b+w*t)or(b<a and b-w*t>=a-v*t):print("YES")
else:print("NO")