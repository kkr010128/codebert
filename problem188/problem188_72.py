X, Y, A, B, C = [int(_) for _ in input().split()]
P = [int(_) * 3 for _ in input().split()]
Q = [int(_) * 3 + 1 for _ in input().split()]
R = [int(_) * 3 + 2 for _ in input().split()]
S = sorted(P + Q + R)
cnt = [0, 0, 0]
ans = [0, 0, 0]
limit = [X, Y, 10**10]
while S:
    s = S.pop()
    q, r = divmod(s, 3)
    if cnt[r] >= limit[r]:
        continue
    cnt[r] += 1
    ans[r] += q
    if sum(cnt) == X + Y:
        print(sum(ans))
        exit()
