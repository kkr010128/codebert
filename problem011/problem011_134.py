
a,b = map(int,input().split())
while True:
    r=a%b
    if r==0:
        break
    else:
        a=b
        b=r
print(b)