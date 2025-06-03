k, n = map(int, input().split())
A = list(map(int, input().split()))
D = []
for i in range(n-1):
    D.append(A[i+1]-A[i])
else:
    D.append(k-(A[n-1]-A[0]))
D.sort(reverse=True)
print(k-D[0])
