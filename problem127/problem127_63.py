x,y=map(int,input().split())

if ((4*x-y)%2==0 and (-2*x+y)%2==0) and (1<=(4*x-y)//2<=100 and 1<=(-2*x+y)//2<=100):
    print('Yes')
elif ((4*x-y)%2==0 and (-2*x+y)%2==0) and (1<=(4*x-y)//2<=100 and (-2*x+y)//2==0):
    print('Yes')
elif ((4*x-y)%2==0 and (-2*x+y)%2==0) and ((4*x-y)//2==0 and 1<=(-2*x+y)//2<=100):
    print('Yes')
else :
    print('No')
