N, K =map(int,input().split())
A = list(map(int,input().split()))
ans = []
for i in range(K,N):
    if (A[i]/A[i-K])>1:
        ans.append("Yes")
    else:
        ans.append("No")

for i in range(len(ans)):
    print(ans[i])