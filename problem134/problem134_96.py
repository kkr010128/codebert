N=int(input())
As=list(map(int,input().split()))
ans=1

if 0 in As:
    print(0)
else:
    for i in range(N):
        ans*=As[i]
        if ans>int(1e18):
            break
    print(ans if ans<=int(1e18) else -1)