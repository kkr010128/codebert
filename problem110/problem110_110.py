A = list(map(int, input().split()))
H = A[0]
W = A[1]
K = A[2]

colors = []
for line in range(H):
    color = input()
    color = list(color)
    colors.append(color)
ans = 0
for i in range(2**H):
    for j in range(2**W):
        cnt = 0
        for k in range(H):
            for l in range(W):
                if list(format(i,"0"+str(H)+"b"))[k] == "0" and list(format(j,"0"+str(W)+"b"))[l] == "0":
                    if colors[k][l] == "#":
                        cnt += 1
        if cnt == K:
            ans+= 1
print(ans)