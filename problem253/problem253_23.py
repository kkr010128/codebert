n,a,b=map(int,input().split())
if (b-a)%2 == 0:
    print((b-a)//2)
else:
    if n-b >= a-1:
        ans = a-1
        ans += (b-a-1)//2
        print(ans+1)
    else:
        ans = n-b
        ans += (b-a-1)//2
        print(ans+1)