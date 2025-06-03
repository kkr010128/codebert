N = int(raw_input())
A = map(int, raw_input().split())
count = 0
for i in range(0, N):
    min_j = i
    c = 0
    for j in range(i, N):
        if A[j] < A[min_j]:
            min_j = j
            c = 1
    A[i], A[min_j] = A[min_j], A[i]
    count += c
print " ".join(map(str, A))
print count