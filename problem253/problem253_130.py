N, A, B = map(int, input().split())

A, B = min(A, B), max(A, B)
d = B - A
if d % 2 == 0:
    print(d // 2)
else:
    if (A - 1 <= N - B):
        A, B = A - 1, B - 1
    else:
        A, B = N - B, N - A
    ans = min(B, A + 1 + (B - A - 1) // 2)
    print(ans)
