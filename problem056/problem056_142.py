[n, m] = [int(x) for x in raw_input().split()]
A = [[0] * m for x in range(n)]
B = [0] * m
counter = 0
while counter < n:
    A[counter] = [int(x) for x in raw_input().split()]
    counter += 1

counter = 0
while counter < m:
    B[counter] = int(raw_input())
    counter += 1

counter = 0
while counter < n:
    result = 0
    for j in range(m):
        result += A[counter][j] * B[j]
    print(result)
    counter += 1