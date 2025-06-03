A = [list(map(int, input().split())) for _ in range(3)]
N = int(input())
B = [int(input()) for _ in range(N)]
for b in B:
    for y in range(3):
        for x in range(3):
            if A[y][x] == b:
                A[y][x] = -1
for y in range(3):
    if sum(A[y]) == -3:
        print("Yes")
        exit()
for x in range(3):
    if A[0][x] == A[1][x] == A[2][x] == -1:
        print("Yes")
        exit()
if A[0][0] == A[1][1] == A[2][2] == -1 or A[2][0] == A[1][1] == A[0][2] == -1:
    print("Yes")
    exit()
print("No")
