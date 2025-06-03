n=int(input())
A=list(map(int,input().split()))

ans=1

if 0 in A:
    print(0)
else :
    for i in range(n):
        ans*=A[i]
        if ans > 10**18:
            break

    if ans>10**18:
        print(-1)
    else :
        print(ans)
