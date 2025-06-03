A = []
hit = []
for _ in range(3):
    A.append(list(map(int, input().split())))
    hit.append([False]*3)

N=int(input())
for _ in range(N):
    b = int(input())
    for i in range(3):
        for j in range(3):
            if A[i][j] == b:
                hit[i][j] = True
                break

for i in range(3):
    if hit[i][0] and hit[i][1] and hit[i][2]:
        print('Yes')
        exit()
    if hit[0][i] and hit[1][i] and hit[2][i]:
        print('Yes')
        exit()
if hit[1][1]:
    if hit[0][0] and hit[2][2] or hit[2][0] and hit[0][2]:
        print('Yes')
        exit()

print('No')
