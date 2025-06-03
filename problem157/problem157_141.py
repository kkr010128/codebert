N = int(input())
A = [int(num) for num in input().split()]

S = {-A[0] : 1}
ans = 0
for i in range(1,N):
    ans += S.get(A[i]-i, 0)
    S[-A[i]-i] = S.get(-A[i]-i, 0) + 1
print(ans)