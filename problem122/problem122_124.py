from collections import Counter
n = int(input())
A = list(map(int, input().split()))
ANS = sum(A)
A = Counter(A)
Q = int(input())
for i in range(Q):
    B, C = map(int, input().split())
    print(ANS + (C - B) * A[B])
    ANS += (C - B) * A[B]
    A[C] = A[C] + A[B]
    A[B] = 0
