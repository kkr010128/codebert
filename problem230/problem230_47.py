N, D, A = map(int, input().split())
XH = sorted([tuple(map(int, input().split())) for _ in range(N)])
ans, r, S, R = 0, 0, [0] * (N + 2), []
for l in range(N):
    while r + 1 < N and XH[r + 1][0] - XH[l][0] <= 2 * D:
        r += 1
    S[l + 1] += S[l]
    bomb = (max(XH[l][1] - S[l + 1], 0) + A - 1) // A
    ans += bomb
    S[l + 1] += bomb * A
    S[r + 1 + 1] -= bomb * A
    R.append(r)
print(ans)
