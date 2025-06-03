n=int(input())
x=0
y=1
if n==0 or n==1:
    print(1)
else:
    for i in range(n):
        x,y=y,x+y
        i+=1
    print(y)
