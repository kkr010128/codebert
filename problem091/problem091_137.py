N = int(input())
A = sorted(map(int, input().split())) 

X = 0
Y = 0

B = []

for i in range(N-2):
    X = i + 1
    for j in range(X,N-1):
        Y = j + 1
        for k in range(Y, N):
            if A[k] < A[i] + A[j]:
                if A[k] != A[i] and A[i] != A[j] and A[k] != A[j]:
                    B.append((A[i],A[j],A[k]))

print(len(B))