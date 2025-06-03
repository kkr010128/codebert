n=int(input())
s=[]
t=[]
flag=0
ans=0
for i in range(n):
    ss,tt=map(str,input().split())
    s.append(ss)
    t.append(int(tt))
x=input()

for i in range(n):
    if s[i]==x:
        flag=1
        continue
    if flag == 1:
        ans+=t[i]
print(ans)