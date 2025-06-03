N = int(input())
ST = []
for i in range(N):
    x, l = list(map(int, input().split()))
    ST.append([x-l, x+l])
ST.sort(key = lambda x :x[1])
startT = ST[0][1]
ans = 1
if N != 1:
    for i in range(1,N):
        if startT <= ST[i][0]:
            startT = ST[i][1]
            ans += 1
            
print(ans)