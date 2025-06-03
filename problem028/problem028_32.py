n,m = map(int,input().split())
C = sorted(map(int,input().split()))


T = [float("inf")]*(n+1)
T[0]= 0

for i in range(m):
    for j in range(C[i],n+1):
        T[j] = min(T[j],T[j-C[i]]+1)

print(T[n])