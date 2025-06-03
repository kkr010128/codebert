N,K=map(int,input().split())
A=list(map(int,input().split()))
B=[N-A[K-1]+A[0]]
for i in range(K-1):
    b=A[i+1]-A[i]
    B.append(b)
B.sort()
print(sum(B)-B[K-1])