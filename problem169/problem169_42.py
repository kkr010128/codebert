N = int(input())
A = list(map(int,input().split()))

buka = [0]*N

for p in range(N-1):
    buka[A[p] -1] += 1

for q in range(N):
    print(buka[q])