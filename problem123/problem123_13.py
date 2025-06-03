N=int(input())
A = list(map(int,input().split()))
val = 0
for i in range(N):
    val = val ^ A[i]

ans = []
for i in range(N):
    s = val ^ A[i]
    ans.append(s)

print(*ans)