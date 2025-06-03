n,m,x = list(map(int,input().split()))

cList = []

for i in range(n):
    cList.append(list(map(int,input().split())))

priceList = []
for i in range(1,2**n):
    price = 0
    check = 1
    skilList = [0 for  i in range(m)]
    bit = i
    for j in range(1,n+1):
        if bit % 2 == 1:
            price += cList[j-1][0]
            for k in range(m):
                skilList[k] = skilList[k] + cList[j-1][k+1]
        bit = bit // 2
    for j in skilList:
        if j < x:
            check = 0
            break
    if check == 1:
        priceList.append(price)

if len(priceList) > 0:
    print(min(priceList))
else:
    print(-1)