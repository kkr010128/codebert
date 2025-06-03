N, M = input().split()
N = int(N)
M = int(M)
A = list(map(int, input().split()))
LA = len(A)
i = 0
SUM = 0

for i in range(LA):
    SUM = SUM + A[i]
    
if SUM > N:
    print('-1')
    
else:
    print(N - SUM)