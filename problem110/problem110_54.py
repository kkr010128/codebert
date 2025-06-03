h,w,k = map(int, input().split())
grid = [input() for _ in range(h)]

ans = 0

for i in range(2**h):
    for j in range(2**w):
        count = 0
        for m in range(h):
            for l in range(w):
                if (i>>m)&1==0 and (j>>l)&1==0 and grid[m][l] == "#":
                    count+=1
        if count == k: ans+=1
print(ans)