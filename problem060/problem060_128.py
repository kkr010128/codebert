N,M,L = (int(i) for i in input().split())
A = [[int(i) for i in input().split()] for i in range(N)]
B = [[int(i)for i in input().split()] for i in range(M)]
C = []
for i in range(N):
    for i2 in range(L):
        ans = 0
        for i3 in range(M):
            ans += A[i][i3]*B[i3][i2]
        if i2 == L-1:
            print(ans)
        else:
            print(ans,end=" ")