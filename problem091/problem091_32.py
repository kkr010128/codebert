n = int(input())
arr = list(map(int, input().split()))
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if arr[i] != arr[j] and arr[i] != arr[k] and arr[j] != arr[k]:
                if (arr[i] + arr[j]) > arr[k] and (arr[i] + arr[k]) > arr[j] and (arr[j] + arr[k]) > arr[i]:
                    ans += 1
print(ans)
