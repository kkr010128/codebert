h, w, k = map(int, input().split())
c = [list(input()) for i in range(h)]

ans = 0
for i in range(1 << h):
    for j in range(1 << w):
        black = 0
        for x in range(h):
            for y in range(w):
                if (i >> x) & 1:
                    continue
                    
                if (j >> y) & 1:
                    continue
                    
                if c[x][y] == '#':
                    black += 1
        if black == k:
            ans += 1
print(ans)
