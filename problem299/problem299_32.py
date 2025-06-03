N=int(input())
A=list(map(int,input().split()))
for i in range(N):
    A[i] = [i+1, A[i]]

A.sort(key=lambda x:x[1])

ans=[]
for i in range(N):
    ans.append(A[i][0])

ans = map(str, ans)
print(' '.join(ans))
