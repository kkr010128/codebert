x=1
while True:
    x=list(input())
    x=map(int,x)
    x=sum(x)
    if x==0:
        break
    print(x)