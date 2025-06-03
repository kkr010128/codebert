
N = int(input())
S = input()

d = {"R": 0, "G": 1, "B": 2}
ctr = [[0] * 3 for _ in range(N + 1)]
for i in range(N):
    ctr[i + 1][d[S[i]]] += 1
    for j in range(3):
        ctr[i + 1][j] += ctr[i][j]


ans = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        if S[i] != S[j]:
            c = (set("RGB") - set([S[i], S[j]])).pop()
            cnt = ctr[-1][d[c]] - ctr[j + 1][d[c]]

            k = 2 * (j + 1) - (i + 1) - 1
            if j < k < N and c == S[k]:
                cnt -= 1

            ans += max(0, cnt)

print(ans)
