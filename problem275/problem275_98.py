x,y=map(int,input().split())
k=[1,2,3]
l=[0,300000,200000,100000]
p=0
if x in k:
  p+=l[x]
if y in k:
  p+=l[y]
if x==1 and y==1:
  p+=400000
print(p)
  

