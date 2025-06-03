N = int(input())
*A, = map(int, input().split())
# N = 5
# A = list([24, 11, 8, 3, 16])

M = max(A) + 1
cnt =[0 for _ in range(M)]

for i in A:
    for j in range(i, M, i):
        cnt[j] += 1

ans = 0
for k in A:
    if cnt[k] == 1:
        ans += 1
print(ans)
