import numpy as np
a = [list(map(int, input().split())) for _ in range(3)]
n = int(input())
b = [int(input()) for i in range(n)]

for i in range(3):
    for j in range(3):
        for k in range(n):
            if a[i][j] == b[k]:
                a[i][j] = 0
c = []
c.append(np.sum(a,axis = 0))
c.append(np.sum(a,axis = 1))
d = np.prod(c)
if d == 0:
    print("Yes")
elif (a[0][0] == 0 and a[1][1] == 0 and a[2][2] == 0) or (a[2][0] == 0 and a[1][1] == 0 and a[0][2] == 0):
    print("Yes")
else:
    print("No")
    

