N = int(input())
a = list(map(int, input().split()))
for i in range(N):
    if i == 0:
        tmp = a[i]
    else:
        tmp = tmp ^ a[i]
ans = []
for i in range(N):
    ans.append(tmp ^ a[i])
print(*ans)