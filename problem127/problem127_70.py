x,y =map(int,input().split())
if y-2*x >=0 and (y-2*x)%2 ==0 and 4*x-y >=0 and (4*x-y)%2 ==0:
    print('Yes')
    exit()
print('No')