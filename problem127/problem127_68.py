a,b=map(int,input().split())

if(b%2==0):
    if(2*a<=b<=4*a):
        print("Yes")
    else:
        print("No")
else:
    print("No")