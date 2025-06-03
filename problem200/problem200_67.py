A,B,M = [int(hoge) for hoge in input().split()]
A = [int(hoge) for hoge in input().split()]
B = [int(hoge) for hoge in input().split()]
ans = min(A) + min(B)
for i in range(M):
    x,y,c = [int(hoge) for hoge in input().split()]
    ans = min(ans,A[x-1]+B[y-1]-c)
print(ans)