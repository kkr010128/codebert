a,b,c = map(int,input().split())
ab= (a*b)*4
C= (c-a-b)**2
if c-a-b>=0:
    if ab<C:
        print("Yes")
    else :
        print("No")
else :
    print("No")
