A = [list(map(int, input().split())) for i in range(3)]

N = int(input())

for n in range(N):
    b = int(input())
    for i in range(3):
        for j in range(3):
            if b == A[i][j]:
                A[i][j] = 0


for i in range(3):
    if A[i] == [0, 0, 0]:
        print('Yes')
        exit()

    vertical = [_[i] for _ in A]

    if vertical == [0, 0, 0]:
        print('Yes')
        exit()

if A[0][0] == A[1][1] == A[2][2] == 0 or A[0][2] == A[1][1] == A[2][0] == 0:
    print('Yes')
    exit()
else:
    print('No')