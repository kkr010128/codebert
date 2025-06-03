N=int(input())
L=list(map(int, input().split()))
L=sorted(L)
import bisect

ans=0
for i in range(N-1):
    for j in range(i+1,N):
        a=L[i]
        b=L[j]
        upper = bisect.bisect_left(L,a+b)
        lower=max(j+1, bisect.bisect_right(L, a-b), bisect.bisect_right(L, b-a))
        #print(upper, lower)
        ans+=max(0, upper-lower)


print(ans)