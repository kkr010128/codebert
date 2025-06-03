N = int(input())
A = list(map(int,input().split()))
A.insert(0,0)
A = [(i,A[i]) for i in range(N+1)]
A = sorted(A,key=lambda x:x[1])
B = []
for i in range(1,N+1):
    B.append(A[i][0])
print(*B)