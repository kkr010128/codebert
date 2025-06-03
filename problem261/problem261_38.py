import math
s=list(input())
N=len(s)
x=0
for i in range(0,N):
    if s[i]!=s[N-1-i]:
        x+=1
x=math.ceil(x/2)
print(x)