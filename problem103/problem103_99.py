N = int(input())
A = list(map(int, input().split()))
ans = 1000
for i in range(N-1):
    if A[i] < A[i+1]:
        temp = ans // A[i]
        ans -= temp*A[i]
        ans += temp*A[i+1]
print(ans)