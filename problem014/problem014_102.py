N = int(raw_input())
A = map(int, raw_input().split())
i = 0
flag = 1
while flag:
    flag = 0
    for j in range(N-1, 0, -1):
        if A[j] < A[j-1]:
            A_j = A[j]
            A[j] = A[j-1]
            A[j-1] = A_j
            flag = 1
            i += 1
print " ".join(map(str, A))
print i