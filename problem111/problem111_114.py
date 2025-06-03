N=int(input())
A=[int(i) for i in input().split()]

A.sort(reverse=True)


if N%2==1:
    if N==3:
        ans=A[0]+A[1]
    else:
        ans=A[0]
        for i in range(1,N//2):
            ans+=A[i]*2
        ans+=A[N//2]
else:
    ans=A[0]
    for i in range(1,N//2):
        ans+=A[i]*2

print(ans)
