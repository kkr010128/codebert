n,m = [int(x) for x in input().split( )]
a = [[0 for x in range(m)] for y in range(n)]
b = []
for i in range(n):
    retsu = [int(x) for x in input().split( )]
    a[i] = retsu
for j in range(m):
    b.append(int(input()))
answer = []
for i in range(n):
    value = 0
    for j in range(m):
        value += a[i][j]*b[j]
    answer.append(value)
for ans in answer:
    print(ans)

