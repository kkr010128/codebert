n,k = map(int,input().split())
a = list(map(int,input().split()))

for i in range(k):
    table = [0 for _ in range(n*2)]
    # imos法
    for j in range(n):
        ai = a[j]
        # 電球が照らす左端
        table[max((j-ai)*2-1,0)] += 1
        # 電球が照らす右端
        table[min((j+ai)*2+1,n*2-1)] -= 1
    # 累積和
    for j in range(n*2):
        if j > 0:
            table[j] += table[j-1]
    for j in range(n):
        a[j] = table[j*2]
    flag = True
    for j in range(n):
        if a[j] != n:
            flag = False
            break
    if flag:
        print(*a)
        exit()
print(*a)