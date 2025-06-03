# Bingo
A = []
for _ in range(3):
    A += list(map(int, input().split()))
N = int(input())
for _ in range(N):
    b = int(input())
    if b in A:
        A[A.index(b)] = -1
        
# check
diag = (sum(A[0::4]) == -3) | (sum(A[2:8:2]) == -3)
rows = (sum(A[:3]) == -3) | (sum(A[3:6]) == -3) | (sum(A[6:]) == -3)
cols = (sum(A[:7:3]) == -3) | (sum(A[1:8:3]) == -3) | (sum(A[2::3]) == -3)
ans = diag | rows | cols
print(['No', 'Yes'][ans])