n, m = map(int, input().split())
A = []
B = []
for line in range(n):
    A.append(list(map(int, input().split())))
for line in range(m):
    B.append(int(input()))
#print(A,B)

ret = []
for i in range(n):
    ret.append(sum(A[i][j] * B[j] for j in range(m)))
print('\n'.join(map(str, ret)))