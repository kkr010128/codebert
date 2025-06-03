A = [[int(i) for i in input().split()] for _ in range(3)]
N = int(input())
for i in range(N) :
    b = int(input())
    for j in range(3) :
        if b in A[j] :
            x = A[j].index(b)
            A[j][x] = 0
        
#print(A)

for i in range(3) :
    if all(A[i][n] == 0 for n in range(3)) or all(A[m][i] == 0 for m in range(3)):
        print('Yes')
        exit()
if A[0][0] == 0 and A[1][1] == 0 and A[2][2] == 0 :
    print('Yes')
    exit()
if A[0][2] == 0 and A[1][1] == 0 and A[2][0] == 0 :
    print('Yes')
    exit()
print('No')