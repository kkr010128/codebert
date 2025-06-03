x,y=map(int,input().split())
c=x%y

while c!=0:
    x=y
    y=c
    c=x%y
print(y)
