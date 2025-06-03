N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(M)]

ans = [10] * N
for l in lst:
    if ans[l[0]-1] < 10 and ans[l[0]-1] != l[1]:
        print(-1)
        exit()
    ans[l[0]-1] = l[1]

if ans[0] == 10:
    if N == 1:
        ans[0] = 0
    else:
        ans[0] = 1
for i in range(1, N):
    if ans[i] == 10:
        ans[i] = 0

if N != 1 and ans[0] == 0:
    print(-1)
    exit()

ans = list(map(str, ans))
print("".join(ans))