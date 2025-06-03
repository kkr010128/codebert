n, m = map(int, input().split())
vector_a = []
vector_b = []
for i in range(n):
    vector_a.append(list(map(int,input().split())))
for i in range(m):
    vector_b.append(list())
    vector_b[i]=int(input())

for i in range(n):
    tmp=0
    for j in range(m):
        tmp+=vector_a[i][j]*vector_b[j]
    print(tmp)