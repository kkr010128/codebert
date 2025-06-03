import math

n,x,t = map(int,input().strip().split(" "))

ans = math.ceil(n/x)
ans = ans*t
print(ans)