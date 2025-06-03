N,A,B=map(int,input().split())
if (B-A)%2==0:
    ans =(B-A)//2
else:
    if A-1 > N-B:
        ans = N-B+1
        A+=ans
        ans+=(N-A)//2
    else:
        ans =A
        B-=ans
        ans+=(B-1)//2
print(ans)
