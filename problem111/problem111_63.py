n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
ans = arr[0]
i = 1
j = 1
while i < n-1:
    ans += arr[j]
    #print (arr[j])
    if i % 2 == 0:
        j += 1
    i += 1
print (ans)