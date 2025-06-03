NM = input().split()
n = int(NM[0])
m = int(NM[1])

A = []
B = []
for i in range(n):
    A.append([])
    a = input().split()
    for j in range(m):
        A[i].append(int(a[j]))

for i in range(m):
    b = int(input())
    B.append(b)

out = []
for i in range(n):
    sum = 0
    for j in range(m):
        sum = sum + A[i][j]*B[j]
    out.append(sum)

for i in range(n):
    print(out[i])