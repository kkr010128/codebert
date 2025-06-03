N = int(input())
A = [int(i) for i in input().split()]

ans = []
for i in range(N):
    ans.append([A[i],i+1])

ans.sort()
for i in range(N-1):
    print(ans[i][1],end=' ')
print(ans[-1][1])
