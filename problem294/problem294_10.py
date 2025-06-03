import bisect
n = int(input())
arr = list(map(int,input().split()))
arr.sort()
ans = 0
for i in range(n-2):
    for j in range(i+1,n-1):
        x = arr[i]+arr[j]
        ind = bisect.bisect_left(arr,x)
        ans+=(ind-j-1)
print(ans)