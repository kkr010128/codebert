p = 10**9+7
N = int(input())
A = list(input().split())
B = [0 for _ in range(N)]
for i in range(N):
    a = A[i]
    b = bin(int(a))[2:]
    b = "0"*(60-len(b))+b
    B[i] = b
C = {i:0 for i in range(60)}
for j in range(60):
    cnt = 0
    for i in range(N):
        if B[i][j]=="1":
            cnt += 1
    C[j] = cnt
tot = 0
for j in range(60):
    n = C[j]
    k = (N*(N-1))//2-(n*(n-1))//2-((N-n)*(N-n-1))//2
    tot = (tot+k*(2**(60-1-j)))%p
print(tot)