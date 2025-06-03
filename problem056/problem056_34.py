N, M = map(int, raw_input().split())
matrix = [map(int, raw_input().split()) for n in range(N)]
array = [input() for m in range(M)]

for n in range(N):
    c = 0
    for m in range(M):
        c += matrix[n][m] * array[m]
    print c