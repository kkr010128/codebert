t1,t2=map(int,input().split())
a1,a2=map(int,input().split())
b1,b2=map(int,input().split())
x,y=t1*(a1-b1),t2*(a2-b2)
if (x+y)==0:
  print("infinity")
elif x*(x+y)>0:
  print(0)
else:
  if x>0:
    x1,x2=x,x+y
  else:
    x1,x2=-x,-(x+y)
  if x1%x2==0:
    print(2*abs(x1//x2))
  else:
    print(2*abs(x1//x2)-1)
