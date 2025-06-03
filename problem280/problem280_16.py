from itertools import permutations
n = int(input())
x = []
y = []
ans,count,tempx,tempy = 0,0,0,0
for _ in range(n):
    a,b = map(int,input().split())
    x.append(a)
    y.append(b)
order = list(permutations(range(n)))
for i in order:
    for j in i:
        if j == i[0]:
            tempx = x[j]
            tempy = y[j]
            continue
        count += (((x[j]-tempx)**2)+((y[j]-tempy)**2)) ** (0.5) 
        tempx = x[j]
        tempy = y[j]
    ans += count / len(order)
    count = 0
print(ans)