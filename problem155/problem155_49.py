n, m = map(int, input().split())
ht = list(map(int, input().split()))
rd = [list(map(int, input().split())) for _ in range(m)]
flg = [1] * n
for i in rd:
    if ht[i[0]-1] <= ht[i[1]-1]:
        flg[i[0]-1] = 0
    if ht[i[0]-1] >= ht[i[1]-1]:
        flg[i[1]-1] = 0
print(sum(flg))