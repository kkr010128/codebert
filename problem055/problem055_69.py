ryou = [0]*4
for i in range(4):
    ryou[i] = [0]*3
for i in range(4):
    for j in range(3):
        ryou[i][j] = [0]*10
sep = '#' * 20

n = int(input())
for i in range(n):
    b, f, r, v = [int(x) for x in input().split()]
    ryou[b-1][f-1][r-1] += v

for i in range(4):
    for j in range(3):
        s = ' '
        s += ' '.join(map(str,ryou[i][j]))
        print(s)
    if not i == 3:
        print(sep)