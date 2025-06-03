H, N = map(int, input().split())
A = list(map(int, input().split()))

SUM = 0
for i in range(len(A)):
    SUM = SUM + A[i]

if SUM >= H:
    print('Yes')
else:
    print('No')