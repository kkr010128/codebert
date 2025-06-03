ichi = input().split()
n = int(ichi[0])
m = int(ichi[1])
a = [[0 for j in range(m)] for i in range(n)]
for i in range(n):
    input_a = input().split()
    for j in range(m):
       a[i][j] = int(input_a[j])
b = []
for i in range(m):
    b.append(int(input()))
for i in range(n):
    c=0
    for j in range(m):
        c += a[i][j] * b[j]
    print(c)