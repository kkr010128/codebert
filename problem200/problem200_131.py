A, B, M = map(int,input().split())
A = [a for a in map(int,input().split())]
B = [b for b in map(int,input().split())]
C = []
for m in range(M):
    C.append([c for c in map(int,input().split())])

ans = min(A) + min(B)

for c in C:
    if (A[c[0]-1]+B[c[1]-1]-c[2])<ans:
        ans = A[c[0]-1]+B[c[1]-1]-c[2]
print(ans)