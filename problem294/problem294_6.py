import bisect

N=int(input())
L=[int(i) for i in input().split()]

L.sort()
ans=0
for i in range(N-2):
    for j in range(i+1,N-1):
        x=L[i]+L[j]
        ans+=(bisect.bisect_left(L,x)-j-1)

print(ans)
