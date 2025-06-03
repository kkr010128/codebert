A = [list(map(int, input().split())) for i in range(3)]
N = int(input())
a = [[False] * 3 for _ in range(3)]
for _ in range(N):
    b = int(input())
    for i in range(3):
        for j in range(3):
            if A[i][j] == b:
                a[i][j] = True
ans = False
for i in range(3):
    if a[i][0] and a[i][1] and a[i][2] or a[0][i] and a[1][i] and a[2][i]:
        print('Yes')
        exit()
if a[0][0] and a[1][1] and a[2][2] or a[2][0] and a[1][1] and a[0][2]:
        print('Yes')
        exit()
print('No')
