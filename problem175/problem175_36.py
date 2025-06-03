N = int(input())
S = [s for s in input()]
ans = S.count("R") * S.count("G") * S.count("B")

for i in range(N - 2):
    for j in range(i + 1, N - 1):
        k = j + (j - i)
        if N - 1 < k:
            continue
        if S[k] != S[i] and S[k] != S[j] and S[i] != S[j]:
            ans -= 1

print(ans)
