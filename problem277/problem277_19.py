h, w, k = map(int, input().split())
s = [""] * h
for i in range(h):
    s[i] = input()

ans = [[0 for i in range(w)] for j in range(h)]
lcnt = [0] * h
cnt = 0

for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            lcnt[i] += 1

flag = 0
mem = [0] * w

a = 1

for i in range(h):
    t = 0
    j = 0

    while t < lcnt[i]:

        if s[i][j] == "#":
            t += 1
            ans[i][j] = a
            a += 1
        else:
            ans[i][j] = a

        j += 1

    for l in range(j, w):
        ans[i][l] = a - 1

for i in range(h):
    if lcnt[i] > 0:
        for j in range(w):
            mem[j] = ans[i][j]
        break

t = 0
while lcnt[t] == 0:
    for i in range(w):
        ans[t][i] = mem[i]
    lcnt[t] = 1
    t += 1

for i in range(1, h):
    if lcnt[i] == 0:
        for j in range(w):
            ans[i][j] = ans[i - 1][j]

for i in range(h):
    for j in range(w):
        print(ans[i][j], end="")
        if j != w - 1:
            print(" ", end="")
    print()