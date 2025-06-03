N = int(input())
A = list(map(int, input().split()))
S = [0]
for i in range(N):
    S.append(A[i] + S[i])
ans = float('inf')
for i in range(1, N):
    ans = min(ans, abs((S[i] - S[0]) - (S[N] - S[i])))
print(ans)
