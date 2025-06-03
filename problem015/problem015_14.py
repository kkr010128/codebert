N = int(raw_input())
A = map(int, raw_input().split())
count = 0
for i in xrange(N):
    minj = i
    for j in xrange(i, N):
        if A[j] < A[minj]:
            minj = j
    if minj != i:
        A[i], A[minj] = A[minj], A[i]
        count += 1
print ' '.join(map(str, A))
print count