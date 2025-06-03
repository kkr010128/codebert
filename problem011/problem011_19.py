def g(n):
 x,y=n
 r=x%y
 if r>0:g((y,r))
 else:print(y)
g(sorted(list(map(int,input().split()))))