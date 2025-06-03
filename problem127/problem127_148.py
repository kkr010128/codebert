X,Y=map(int,input().split())
a=[]
for i in range(0,X+1):
    if i*2+(X-i)*4==Y:
        a.append('Yes')
    else:
        continue
if 'Yes' in a:
    print('Yes')
else:
    print('No')