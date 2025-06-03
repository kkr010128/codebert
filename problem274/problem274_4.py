n,m=map(int,input().split())
s=input()
x=n
a=[]
while x!=0:
  for i in range(min(m,x),0,-1):
    if s[x-i]=="0":a.append(i);break
    if i==1:print(-1);exit()
  x-=i
print(*a[::-1])