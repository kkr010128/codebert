N, K, S = map(int, input().split())
if S == 10 ** 9:
    ans = [S] * K + [S - 1] * (N - K)
else:
    ans = [S] * K + [10 ** 9] * (N - K)

for i in range(N):
    if i != N - 1:
        print(ans[i], end = ' ')
    else:
        print(ans[i])