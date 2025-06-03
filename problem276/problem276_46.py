n = int(input())
arr = list(map(int,input().split()))

tot = sum(arr)

temp = 0
ans = 1e18
for i in range(n):
    temp += arr[i]
    rest = tot-temp
    cost = abs(rest-temp)
    if cost < ans:
        ans = cost

print(ans)