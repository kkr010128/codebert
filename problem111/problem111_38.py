N = int(input())
A = list(map(int, input().split()))
A = sorted(A, reverse = True)

L = len(A) // 2

if len(A) % 2 == 0:
    #偶数の時
    ans = sum(A[:L]) + sum(A[1:L])
else:
    #奇数の時
    ans = sum(A[:L]) + sum(A[1:L+1])

print(ans)
