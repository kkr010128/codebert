n=int(input())
a=list()
for i in range(n):
    s,t=input().split()
    a.append([s,int(t)])
x=input()
flag=False
ans=0
for i in a:
    if flag:
        ans+=i[1]
    if i[0]==x:
        flag=True
print(ans)