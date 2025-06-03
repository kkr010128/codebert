S, T = [input() for i in range(2)]
ans = float("inf")
for start in range(len(S) - len(T) + 1):
    diff = 0
    for t, s in zip(T, S[start:]):
        if t != s:
            diff += 1
    ans = min(ans, diff)
print(ans)
