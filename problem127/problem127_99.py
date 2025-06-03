a=0
X,Y=map(int,input().split())
for i in range(X+1):
    for j in range(X+1-i):
        if 2*i+j*4==Y and i+j==X:
           a=1
if a==1:
    print('Yes')
else:
    print('No')