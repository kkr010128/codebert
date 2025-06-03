#B
N = int(input())
A = list(sorted(map(int,input().split())))
ans=1
if A[0]==0:
    print(0)
else:
    for i in A:
        ans*=i
        if ans > 10**18:
            ans =-1
            break
    print(ans)