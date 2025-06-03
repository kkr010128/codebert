N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

ans = 1
mod = 10 ** 9 + 7

if 0 <= A[0]:
    # All the values are positive -> Use the highest values
    for i in range(N - 1, N - K - 1, -1):
        ans = (ans * A[i]) % mod
elif A[-1] <= 0:
    # All the values are negative -> Check if the result becomes positive or negative
    if K % 2:
        # The result becomes negative -> Use the highest values
        for i in range(N - 1, N - K - 1, -1):
            ans = (ans * A[i]) % mod
    else:
        # The result becomes negative -> Use the highest values
        for i in range(K):
            ans = (ans * A[i]) % mod
else:
    # There exist both positive and negative values
    # If K is an odd number, make K even by extracting A[-1] in advance
    l, r = 0, N - 1
    if K % 2:
        ans = A[-1]
        r -= 1
        K -= 1
    # Compare A[l] * A[l + 1] and A[r -1] * A[r] -> use the bigger one
    # Why: a single negative value makes the result negative
    while K:
        if A[l] * A[l + 1] < A[r] * A[r - 1]:
            ans = (ans * A[r] * A[r - 1]) % mod
            r -= 2
        else:
            ans = (ans * A[l] * A[l + 1]) % mod
            l += 2
        K -= 2

print(ans)
