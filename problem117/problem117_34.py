N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
idx_B = M-1
m = sum(B)
an = M
ans = 0
for a in [0] + A:
    m += a
    while idx_B >= 0 and m > K:
        m -= B[idx_B]
        idx_B -= 1
        an -= 1
    if m > K:
        break
    if an > ans:
        ans = an
    an += 1
print(ans)
