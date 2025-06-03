n = int(input())
A = sorted(map(int, input().split()), reverse=True)
if n % 2 == 0:
    ans = A[0] + 2 * sum(A[1:n//2])
else:
    ans = A[0] + 2 * sum(A[1:n//2]) + A[n//2]
print(ans)