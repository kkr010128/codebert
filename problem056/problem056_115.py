n,m = map(int,raw_input().split())
A = [[0 for i in range(m)] for i in range(n)]
B = [ 0 for i in range(m)]


for i in range(n):
    A[i] = map(int,raw_input().split())
for i in range(m):
    B[i] = input()

for i in range(n):
    sum = 0
    for j in range(m):
        sum += A[i][j] * B[j] 
    print sum