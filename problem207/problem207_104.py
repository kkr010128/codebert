A = [list(map(int,input().split())) for _ in range(3)]
N = int(input())
B = [[0 for _ in range(3)] for _ in range(3)]
for _ in range(N):
    b = int(input())
    for i in range(3):
        for j in range(3):
            if A[i][j]==b:
                B[i][j] = 1
flag = 0
for i in range(3):
    if sum(B[i])==3:
        flag = 1
        break
for j in range(3):
    cnt = 0
    for i in range(3):
        cnt += B[i][j]
    if cnt==3:
        flag = 1
        break
if B[0][0]+B[1][1]+B[2][2]==3:
    flag = 1
if B[2][0]+B[1][1]+B[0][2]==3:
    flag = 1
if flag==1:
    print("Yes")
else:
    print("No")