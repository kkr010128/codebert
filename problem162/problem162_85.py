N, M = map(int, input().split())
matches = []
i = 1
l = N // 2 - 1 if N % 2 == 0 else N // 2
while len(matches) < M:
    if l <= 0:
        i = N // 2 + 1 if N % 2 == 0 else N // 2 + 2
        l = N // 2 - 2 if N % 2 == 0 else N // 2 - 1
        continue
    matches.append((i, i+l))
    i += 1; l -= 2
for a, b in matches: print(a, b)