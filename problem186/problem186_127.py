K, N = map(int, input().split())
A = list(map(int, input().split()))
li = []
for i in range(N):
    if i == 1:
        cadA = A[N-1] - A[0]
    else:
        cadA = K - A[i] + A[i-1]
    if i == N-1:
        cadB = A[N-1] - A[0]
        cadB = 100000000000
    else:
        cadB = A[i] + (K - A[i+1])
        cadB = 100000000000
    li.append(min(cadA, cadB))
print(min(li))