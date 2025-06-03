a,b,c= map(int,input().split())
if c>a+b and 4*a*b<(c-a-b)*(c-a-b):
    print('Yes')
else:
    print('No')