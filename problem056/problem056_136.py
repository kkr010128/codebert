n,m = map(int,input().split())
kakeru = [list(map(int,input().split())) for _ in range(n)]
kakerareru = [int(input()) for _ in range(m)]
for a in range(n):
    kotae = 0
    for b in range(m):
        kotae += kakeru[a][b]*kakerareru[b]
    print(kotae)