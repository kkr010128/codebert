n=int(input())

if n%2==1:
    print(0)
else:
    cnt=1
    ans=0
    while 2*5**cnt<=n:
        ans+=n//(2*5**cnt)

        cnt+=1
    print(ans)
