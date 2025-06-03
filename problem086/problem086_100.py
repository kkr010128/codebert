n,x,t=[int(i) for i in input().split()]
k=n//x
if n%x:
    print((k+1)*t)
else:
    print(k*t)