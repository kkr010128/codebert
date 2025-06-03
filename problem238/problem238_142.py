N, K, S = map(int, input().split())

rem = S + 1

if rem > 10 ** 9:
    rem = 1

ans = []
for i in range(N):
    if i < K:
        ans.append(str(S))
    else:
        ans.append(str(rem))

print(" ".join(ans))
