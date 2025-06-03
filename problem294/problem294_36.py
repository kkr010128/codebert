import bisect as bs
N = int(input())
L = list(map(int,input().split()))
L.sort()
ans = 0
for i in range(len(L)-1):
    for j in range(i+1, len(L)):
        ans += bs.bisect_left(L, L[i]+L[j])-j-1
print(ans)