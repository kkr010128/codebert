S, T = [input() for _ in range(2)]
cnt = 0
for i, c in enumerate(S):
    if c != T[i]:
        cnt += 1

print(cnt)