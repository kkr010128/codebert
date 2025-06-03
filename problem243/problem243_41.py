N = int(input())

M = []

for _ in range(N):
    s, t = input().split()
    M.append((s, int(t)))

X = input()

res = sum(map(lambda m: m[1], M))

for m in M:
    res -= m[1]
    if X == m[0]:
        break

print(res)
