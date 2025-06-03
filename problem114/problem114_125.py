d=int(input())
*c,=map(int, input().split())
s=[]
for _ in range(d):
    *si,=map(int, input().split())
    s.append(si)
t=[int(input())-1 for _ in range(d)]
last=[-1]*26
smx=0
ss=0
for i in range(d):
    ss+=s[i][t[i]]
    last[t[i]]=i
    for j in range(26):
        ss-= c[j]*(i-last[j])
    print(ss)



