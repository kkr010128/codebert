import math
S=list(input())
N=len(S)
a=0
for i in range(0,N):
    if S[i]!=S[N-1-i]:
        a+=1
a=math.ceil(a/2)
print(a)