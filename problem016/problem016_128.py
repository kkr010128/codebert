# -*- coding: utf-8 -*-

N = int(raw_input())
A = map(str, raw_input().split())
B = A[:]
for i in range(N):
    for j in range(N-1, i, -1):
        if int(A[j][1]) < int(A[j-1][1]):
            A[j], A[j-1] = A[j-1], A[j]
bubble = " ".join(A)
for i in range(N):
    minj = i
    for j in range(i, N):
        if int(B[j][1]) < int(B[minj][1]):
            minj = j
    B[i], B[minj] = B[minj], B[i]
select = " ".join(B)
print bubble
print "Stable"
print select
if bubble == select:
    print "Stable"
else:
    print "Not stable"