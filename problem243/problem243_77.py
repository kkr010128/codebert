n=int(input())
s=[""]*n
t=[0]*n
for i in range(n):
    s[i],t[i]=input().split()
    t[i]=int(t[i])
x=input()
c=0
for i in range(n):
    if s[i]==x:
        c=i
        break
ans=0
for i in range(c+1,n):
    ans+=t[i]
print(ans)