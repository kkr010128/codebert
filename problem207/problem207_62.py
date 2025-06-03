

def checkBingo(A,c):
    for i in range(3):
        for j in range(3):
            if A[i][j]==c:
                A[i][j]=0

    for i in range(3):
        if max(A[i])==0 :
            return 1
    for i in range(3):
        if A[0][i]==0 and A[1][i]==0 and A[2][i]==0:
            return 1
    if A[0][0]==0 and A[1][1]==0 and A[2][2]==0:
        return 1
    if A[0][2]==0 and A[1][1]==0 and A[2][0]==0:
        return 1
    return 0

A=[]
for i in range(3):
    A.append( list(map(int,input().split()) ))

# print(A, min(A[0]),min(A[1]),min(A[2]))
n = int(input())

res=0
for i in range(n):
    b = (int(input()))
    # print(A)
    res += checkBingo(A,b)

if res :
    print("Yes")
else:
    print("No")