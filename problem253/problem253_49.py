n,a,b = map(int,input().split())
if abs(a-b)%2 == 0:
    print(abs(a-b)//2)
else:
    if a - 1 > n - b:
        print((n-b+n-a+1)//2)
    else:
        print((a-1+b-1+1)//2)