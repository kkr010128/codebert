n,d=map(int,input().split())

x=[0]*n
y=[0]*n
flag=0

for i in range(n):
  x[i],y[i]=map(int,input().split())
  if (x[i]**2+y[i]**2 <= d**2):
    flag+=1
  
print(flag)