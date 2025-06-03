H,W,k = map(int, input().split())
cell = [input() for i in range(H)]

cnt = 0

for h in range(1 << H):
    for w in range(1 << W):
        black = 0

        for i in range(H):
            if (h >> i) % 2 == 1:
                continue
            for j in range(W):
                if (w >> j) % 2 == 1:
                    continue

                black += cell[i][j] == '#'
        
        cnt += black == k

print(cnt)
            

    
