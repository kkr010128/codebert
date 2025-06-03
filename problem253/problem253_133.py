n,a,b = map(int,input().split())
dif1 = abs(a-b)

if(dif1%2==0):
    print(dif1//2)
else:
    dif2 = (a-1) + (b-1) + 1
    dif3 = (n-a) + (n-b) + 1
    print(min(dif2//2,dif3//2))