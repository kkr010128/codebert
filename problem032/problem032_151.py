n = int(input())
tbl = [[0 for i in range(n)] for j in range(5)]
for i in range(2):
    a = list(map(int,input().split()))
    for j in range(n):
        tbl[i][j] = a[j]
D_1 = 0
d_2 = 0
d_3 = 0
for k in range(n):
    tbl[2][k] = abs(tbl[0][k]-tbl[1][k])
    tbl[3][k] = (abs(tbl[0][k]-tbl[1][k]))**2
    tbl[4][k] = (abs(tbl[0][k]-tbl[1][k]))**3
    D_1 += tbl[2][k]
    d_2 += tbl[3][k]
    d_3 += tbl[4][k]
M = max(tbl[2])
print(f'{D_1:.6f}')
print(f'{(d_2)**(1/2):.6f}')
print(f'{(d_3)**(1/3):.6f}')
print(f'{M:.6f}')
