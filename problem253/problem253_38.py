n,a,b=map(int,input().split())
if (b-a)%2==0:
    print((b-a)//2)
else:
    ans1=min(b-1,n-a)
    ans2=0
    kyori=b-a-1
    ans2+=min(a-1,n-b)+1
    ans2+=kyori//2
    print(min(ans1,ans2))