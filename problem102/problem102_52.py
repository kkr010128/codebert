N, K = map(int, input().split())
A = list(map(int, input().split()))

l = 0
r = l + K
while r < N:
    ans = 'Yes' if A[l] < A[r] else 'No'
    print(ans)
    l += 1
    r += 1
