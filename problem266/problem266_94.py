N = int(input())
C = [100+i for i in range(6)]
T = [float('inf')]*(N+1)
T[0] = 0

for i in range(6):
    for j in range(C[i], N+1):
        T[j] = min(T[j], T[j - C[i]] + 1)

if T[N] != float('inf'):
    print(1)
else:
    print(0)