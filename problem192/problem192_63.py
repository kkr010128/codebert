import numpy as np
n = int(input())
a = list(map(int,input().split()))
s = np.zeros(n+1)
for i in a:
    s[i]+=1
al = sum((s*(s-1))/2)
for i in range(n):
    ans=al-(s[a[i]]-1)
    print(int(ans))