N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
ans = 0
ans = A[0] + sum(A[1:N//2])*2
if N % 2 == 1:
    ans += A[N//2]
# print(A[1:N//2])
# スコアを獲得できるのはN-1回
print(ans)
