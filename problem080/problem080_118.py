n = int(input())
xy  = [list(map(int, input().split())) for _ in range(n)]

xy.sort()
lstm = []
lstp = []
for x, y in xy:
    lstm.append(x-y)
    lstp.append(x+y)
    
lstm.sort()
lstp.sort()
ans = max(lstm[-1] - lstm[0], lstp[-1] - lstp[0])
print(ans)