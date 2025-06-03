r, c = list(map(int, input().split()))
A = []
for i in range(r):
    A.append(list(map(int, input().split())))
    A[i].append(sum(A[i]))
A.append([])
for j in range(c):
    A[r].append(sum(A[i][j] for i in range(r)))
A[r].append(sum(A[r]))
for i in range(r + 1):
    print(" ".join(list(map(str, A[i]))))