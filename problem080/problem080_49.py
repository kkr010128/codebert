n = int(input())
arr = []
for i in range(n):
    x,y = list(map(int,input().split()))
    arr.append((x,y))
arr = sorted(arr)
ans = 0
pre = 1e10
for i in range(n):
    ans = max(ans, arr[i][0] + arr[i][1] - pre)
    pre = min(pre, arr[i][0] + arr[i][1])
pre = 1e10
for i in range(n):
    ans = max(ans, arr[i][0] - arr[i][1] - pre)
    pre = min(pre, arr[i][0] - arr[i][1])
print(ans)