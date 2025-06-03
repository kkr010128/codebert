a = []
for i in range(3):
    l,m,n = map(int,input().split())
    a.append([l,m,n])
n = int(input())
b = []
for i in range(n):
    b.append(int(input()))
#print(a)
#print(b)
for i in range(3):
    for j in range(3):
        for k in range(n):
            if a[i][j] == b[k]:
                a[i][j] = 0
tmp = 0
for i in range(3):
    if a[i][0]+a[i][1]+a[i][2] == 0:
        tmp = 1
    elif a[0][i]+a[1][i]+a[2][i] == 0:
        tmp = 1
if a[0][0]+a[1][1]+a[2][2] ==0:
    tmp = 1
elif a[0][2]+a[1][1]+a[2][0] ==0:
    tmp = 1
if tmp == 1:
    print('Yes')
else:
    print('No')
