
x,y=map(int,input().split())

a=1

while a!=0:
    if x>y:
        a=x%y
    else:
        a=y%x
    x=y
    y=a

print(x)
