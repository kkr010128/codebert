A = []
for i in [0]*3:
    A.append(list(map(int,input().split())))
N = int(input())
B = []
for i in [0]*N:
    B.append(int(input()))

for b in B:
    for i in range(3):
        for j in range(3):
            if A[i][j] == b:
                A[i][j] = -1

#ヨコ
for i in range(3):
    if A[i] == [-1,-1,-1]:
        print("Yes")
        exit()
#タテ
for i in range(3):
    if [A[0][i],A[1][i],A[2][i]] == [-1,-1,-1]:
        print("Yes")
        exit()
#ナナメ
if [A[0][0],A[1][1],A[2][2]] == [-1,-1,-1]:
    print("Yes")
    exit()
if [A[0][2],A[1][1],A[2][0]] == [-1,-1,-1]:
    print("Yes")
    exit()
print("No")
