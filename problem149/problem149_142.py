n,m,x = map(int,input().split())
price = []
A = []
for i in range(n):
    l = list(map(int,input().split()))
    price.append(l[0])
    A.append(l[1:])
# print(A,price)

mini = 10**7

for biti in range(1<<n):
    comprehension = [0]*m
    value = 0
    for i in range(n):
        if (biti >> i & 1):
            for j in range(m):
                comprehension[j] += A[i][j]
            value += price[i]
    flag = True
    for com in comprehension:
        if com < x:
            flag = False
    if flag:
        mini = min(mini,value)
if mini == 10**7:
    print(-1)
else:
    print(mini)