N,M = list(map(int,input().strip().split()))

K = N//2
ans = []

if N == 3:
    ans = [(1,2)]
elif N == 4:
    ans = [(1,2)]
elif N == 5:
    ans = [(1,2),(3,5)]
else:
    left = 1
    right = K
    while left<right:
        ans += [(left,right)]
        left+=1
        right-=1

    left = K+1
    right = N
    if (right-left)%2 == (K-1)%2:
        right -= 1
    while left<right:
        ans += [(left,right)]
        left += 1
        right -= 1

for i in range(M):
    print(ans[i][0],ans[i][1])
