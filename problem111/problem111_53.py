N = int(input())
A = sorted(list(map(int, input().split())), reverse=True)
n = N // 2
if N % 2 == 1:
  ans = sum(A[:n]) + sum(A[1:n+1])
else:
  ans = sum(A[:n]) + sum(A[1:n])
print(ans)