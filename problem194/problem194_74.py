H,W = map(int,input().split())

s = []

for i in range(H):

    S = list(input())
    s.append(S)

dis = [[float("inf")] * W for i in range(H)]

if s[0][0] == "#":
    dis[0][0] = 1
else:
    dis[0][0] = 0

for i in range(H):

    for j in range(W):

        if i != H-1:

            if s[i][j] == "." and s[i+1][j] == "#":

                dis[i+1][j] = min(dis[i][j] + 1,dis[i+1][j])

            else:
                dis[i+1][j] = min(dis[i][j],dis[i+1][j])

        if j != W-1:
            if s[i][j] == "." and s[i][j+1] == "#":

                dis[i][j+1] = min(dis[i][j] + 1,dis[i][j+1])

            else:
                dis[i][j+1] = min(dis[i][j],dis[i][j+1])

print (dis[-1][-1])
