N, M = map(int, raw_input().split())
matrix = []
array = []
for n in range(N):
    tmp = map(int, raw_input().split())
    if len(tmp) > M:
        print 'error'
    matrix.append(tmp)

for m in range(M):
    tmp = input()
    array.append(tmp)

for n in range(N):
    multi = 0
    for m in range(M):
        multi += matrix[n][m] * array[m]
    print multi