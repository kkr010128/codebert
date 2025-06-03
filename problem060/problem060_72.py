n, m, l = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
B = [list(map(int, input().split())) for _ in range(m)]
ans = []
for i in range(n):
    new_row = []
    for j in range(l):
        tmp_ans = 0
        for k in range(m):
            tmp_ans += A[i][k] * B[k][j]
        new_row.append(tmp_ans)
    ans.append(new_row)

for i in range(n):
    print(' '.join(str(x) for x in ans[i]))