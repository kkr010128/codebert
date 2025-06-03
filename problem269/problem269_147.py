t1,t2=map(int,input().split())
a1,a2=map(int,input().split())
b1,b2=map(int,input().split())
x=(a1-b1)*t1
y=(a2-b2)*t2
if x+y==0:
  print('infinity')
elif x*(x+y)>0:
  print(0)
else:
  k=x//(-x-y)
  if x%(-x-y)==0:
    print(k*2)
  else:
    print(k*2+1)