data = list(map(int, input().split()))
n = int(input())
dice = ['12431', '03520', '01540', '04510', '02530', '13421']
for i in range(n):
    up, front = map(int, input().split())
    u = data.index(up)
    f = data.index(front)
    a = dice[u].find(str(f))
    print(data[int(dice[u][a+1])])