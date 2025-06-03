K, N= map(int, input().split())
A = list(map(int, input().split()))
max=K-(A[N-1]-A[0])
for i in range(N-1):
    a=A[i+1]-A[i]
    if max<a:
        max=a
print(K-max)