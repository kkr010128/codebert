import numpy as np
last=[0]*26
D=int(input())
c=list(map(int, (input().split(' '))))
s=[]
a=[0]*D

sat=0

for i in range(D):
    s.append(list(map(int, (input().split(' ')))))
for i in range(D):
    a[i]=int(input())
    last[a[i]-1] = i+1
    sat += s[i][a[i]-1] - np.dot(c, list(map(lambda x: i+1-x, last)))
    print(sat)