N = int(input())
A = list(map(int,input().split()))
B = [0 for _ in range(N//2)]
for i in range(0,N,2):
    B[i//2] = A[i]^A[i+1]
tot = 0
for i in range(N//2):
    tot = tot^B[i]
X = [0 for _ in range(N)]
for i in range(N//2):
    y = tot^B[i]
    X[2*i]=A[2*i+1]^y
    X[2*i+1]=A[2*i]^y
print(*X)