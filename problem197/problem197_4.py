a,b,c=map(int,input().split())
if c<a+b:
    print("No")
    exit()

if 4*a*b<(c-a-b)*(c-a-b):
    print("Yes")
else:
    print("No")
