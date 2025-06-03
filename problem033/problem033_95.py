N = list(map(int,input().split()))
S = list(input())
for i in S:
    if i == "E":
        N[0],N[2],N[3],N[5] = N[3],N[0],N[5],N[2]
    elif i == "W":
        N[3],N[0],N[5],N[2] = N[0],N[2],N[3],N[5]
    elif i == "S":
        N[0],N[1],N[4],N[5] = N[4],N[0],N[5],N[1]
    else:
        N[4],N[0],N[5],N[1] = N[0],N[1],N[4],N[5]
print(N[0])
