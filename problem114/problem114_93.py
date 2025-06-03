d=int(input())
c = list(map(int,input().split()))

s=[None]*d
for i in range(d):
    s[i] = list(map(int,input().split()))
t=[0]*d
for i in range(d):
    t[i]=int(input())

last=[0]*26
satis=0
pena=0
for j in range(d):
    ss=s[j]
    tt=t[j]
    satis += ss[tt-1]
    
    last[tt-1]=j+1
    
    pena += sum(c[i]*(j+1-last[i]) for i in range(26))
    print(satis-pena)