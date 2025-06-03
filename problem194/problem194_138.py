h, w = map(int, input().split())
s = [input() for _i in range(h)]
visit = [[float("inf") for _ in range(w)] for _j in range(h)]
visit[0][0] = 0
for i in range(h):
    for j in range(w):
        if i-1 >= 0:
            visit[i][j] = visit[i-1][j]+(s[i][j]!=s[i-1][j])
        if j-1 >= 0:
            visit[i][j] = min(visit[i][j], visit[i][j-1]+(s[i][j]!=s[i][j-1]))

if s[0][0]==s[h-1][w-1]==".":
    print(visit[h-1][w-1]//2)
elif s[0][0]==s[h-1][w-1]=="#":
    print(visit[h-1][w-1]//2 +1) 
else:
    print(visit[h-1][w-1]//2 +1)