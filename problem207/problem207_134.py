ri = lambda S: [int(v) for v in S.split()]

S = [ri(input()) for _ in range(3)]
N = int(input())
D = set()
O = set()

def mark(A, v):
    for i in range(3):
        for j in range(3):
            if A[i][j] != 0 and A[i][j] == v:
                A[i][j] = 0
                if (i, j) in [(0, 0), (1, 1), (2,2)]:
                    D.add((i,j))
                if (i, j) in [(0, 2), (1, 1), (2, 0)]:
                    O.add((i, j))

for _ in range(N):
    b = int(input())
    mark(S, b)

R = [sum(r) for r in S]
C = [sum(r) for r in zip(*S)]



check = len(D) == 3 or len(O) == 3 or any(v == 0 for v in R) or any(v == 0 for v in C)

print("Yes" if check else "No")
