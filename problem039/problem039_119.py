x=input().split()
y=list(map(int,x))
a=y[0]
b=y[1]
c=y[2]
if a < b and b < c:
 print('Yes')
else:
 print('No')