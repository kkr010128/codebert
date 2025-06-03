import random
d=int(input())
c=list(map(int,input().split()))
s=[list(map(int,input().split())) for _ in range(d)]

#print(d,c,s)
t=[int(input()) for _ in range(d)]

cnt=0
last=[0]*27

for i in range(d):
    cnt+=s[i][t[i]-1]
    last[t[i]-1]=i+1
    for j in range(26):
        cnt-=c[j]*(i+1-last[j])
    
    print(cnt)






