n, m, x = map(int,input().split())
CA = [list(map(int, input().split())) for i in range(n)]
ch = [0]*m
res = 10**5*12 + 5
for i in range(2**n):
    money = 0
    ch = [0]*m
    for j in range(n):
        if ((i >> j) & 1):
            money += CA[j][0]
            for k in range(m):
                ch[k] += CA[j][k+1]
    if min(ch) >= x:
        res= min(money,res)
if res == 10**5*12 + 5:
    print(-1)
else:
    print(res)