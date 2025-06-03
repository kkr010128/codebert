h, w, k = map(int, input().split())

board = [list(input()) for _ in range(h)]

ans = 0

for point_h in range(2**h):
    for point_w in range(2**w):
        cnt=0
        for i in range(h):
            for j in range(w):
                if (point_h>>i)&1==0 and (point_w>>j)&1==0:
                    if board[i][j]=="#":
                        cnt+=1
        if k==cnt:
            ans+=1

print(ans)