[n, m] = [int(x) for x in raw_input().split()]
A = []

counter = 0
while counter < n:
    A.append([int(x) for x in raw_input().split()])
    counter += 1

B = [int(raw_input()) for j in range(m)]

counter = 0
while counter < n:
    result = 0
    for j in range(m):
        result += A[counter][j] * B[j]
    print(result)
    counter += 1