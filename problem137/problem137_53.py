N = int(input())
A = [0]*N
B = [0]*N

for n in range(N):
    A[n],B[n] = map(int,input().split())

A.sort()
B.sort()
if N % 2 == 1:
    print(B[N//2]-A[N//2]+1)
else:
    Am = (A[N//2]+A[N//2-1])/2
    Bm = (B[N//2]+B[N//2-1])/2
    print(int((Bm-Am)*2)+1)