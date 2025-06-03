N = int(input())
alist = list(map(int, input().split()))
gokei = 0
for i in range(0,N):
    for j in range(i+1,N):
        kaihuku = alist[i]*alist[j]
        gokei += kaihuku
print(gokei)