N, M = map(int, input().split())
ans = []
if N % 2 == 1:
    l, r = 1, N - 1
    while l < r:
        ans.append((l, r))
        l += 1
        r -= 1
else:
    l, r = 1, N - 1
    flag = False
    while l < r:
        if not flag and r - l <= N // 2:
            r -= 1
            flag = True
        ans.append((l, r))
        l += 1
        r -= 1
for i in range(M):
    print(ans[i][0], ans[i][1])