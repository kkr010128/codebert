n = int(input())
array = [input().split() for i in range(n)]
S = []
H = []
C = []
D = []
for i in range(1,14):
    S.append(i)
    H.append(i)
    C.append(i)
    D.append(i)
for i in range(n):
    if array[i][0] == "S":
        S[int(array[i][1])-1]=" "
    elif array[i][0] == "H":
        H[int(array[i][1])-1]=" "
    elif array[i][0] == "C":
        C[int(array[i][1])-1]=" "
    else:
        D[int(array[i][1])-1]=" "
for i in range(13):
    if S[i] != " ":
        print("S "+str(S[i]))
for i in range(13):
    if H[i] != " ":
        print("H "+str(H[i]))
for i in range(13):
    if C[i] != " ":
        print("C "+str(C[i]))
for i in range(13):
    if D[i] != " ":
        print("D "+str(D[i]))