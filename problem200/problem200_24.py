a,b,m = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

ans = []
ans.append(min(A)+min(B))


for i in range(m):
    M = list(map(int,input().split()))
    tmp = A[M[0]-1] + B[M[1]-1] -M[2]
    ans.append(tmp)

print(min(ans))
