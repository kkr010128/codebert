#A
H,W = map(int,input().split())
G = [list(str(input())) for _ in range(H)]
inf = float("inf")

dist = [[inf for w in range(W)] for h in range(H)]

if G[0][0] == "#":
    dist[0][0] = 1
else:
    dist[0][0] = 0

for i in range(H):
    for j in range(W):
        if i == 0 and j == 0:
            pass
        elif j == 0:
            dist[i][j] = dist[i-1][j]
            if G[i][j] == "#" and G[i-1][j] != "#":
                dist[i][j]+=1
        elif i == 0:
            dist[i][j] = dist[i][j-1]
            if G[i][j] == "#" and G[i][j-1] != "#":
                dist[i][j]+=1
        else:
            d1 = dist[i-1][j]
            d2 = dist[i][j-1]
            if G[i][j] == "#" and G[i-1][j] != "#":
                d1+=1
            if G[i][j] == "#" and G[i][j-1] != "#":
                d2+=1
            dist[i][j] = min(d1,d2)
        

print(dist[H-1][W-1])

