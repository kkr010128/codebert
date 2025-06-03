k,n = map(int, input().split())
arr = list(map(int, input().split()))
prev = 0
m = 0
for i in arr:
    m = max(m, abs(prev-i))
    prev = i

m = max(m, k+arr[0]-arr[n-1])
ans = k-m
print(ans)