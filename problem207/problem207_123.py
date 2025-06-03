A = [list(map(int, input().split())) for i in range(3)]
N = int(input())

for k in range(N):
    B = int(input())
    for l in range(3):
        for m in range(3):
            if A[l][m] == B:
                A[l][m] = 0

if (A[0][0] == A[0][1] == A[0][2] == 0) or (A[1][0] == A[1][1] == A[1][2] == 0) or (A[2][0] == A[2][1] == A[2][2] == 0):
    print ("Yes")
elif (A[0][0] == A[1][0] == A[2][0] == 0) or (A[0][1] == A[1][1] == A[2][1] == 0) or (A[0][2] == A[1][2] == A[2][2] == 0):
    print ("Yes")
elif (A[0][0] == A[1][1] == A[2][2] == 0) or (A[0][2] == A[1][1] == A[2][0] == 0):
    print ("Yes")
else:
    print ("No")