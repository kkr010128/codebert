n, k = list(map(int, input().split()))
r, s, p = list(map(int, input().split()))

t = input()
last = ["" for _ in range(k)]
move = {"r": "p", "p": "s", "s": "r"}
pts = {"r": r, "p": p, "s": s}
score = 0

for i in range(n):
    if move[t[i]] != last[i%k]:
        score += pts[move[t[i]]]
        last[i%k] = move[t[i]]
    else:
        last[i%k] = ""

print(score)