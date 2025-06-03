h, w, k = map(int, input().split())
s = [list(input()) for _ in range(h)]

ans = [[0] * w for _ in range(h)] 
start = 0
x = 1
cnt = 0

def sol(ans, s, x):
    cnt = 0
    start = 0
    for i in range(len(s)):
        if s[i].count("#") != 0:
            y = i
            break

    for i in range(w):
        if s[y][i] == "#":
            cnt += 1

        if i == w - 1 or (cnt == 1 and s[y][i + 1] == "#"):
            for a in range(len(s)):
                for b in range(start, i + 1):
                    ans[a][b] = x
            start = i + 1
            x += 1
            cnt = 0
    return x


for i in range(h):

    if s[i].count("#") >= 1:
        cnt += 1
    if  i == h - 1 or cnt == 1 and s[i + 1].count("#") >= 1:
        x = sol(ans[start: i + 1], s[start: i + 1], x)
        start = i + 1
        cnt = 0

for i in range(h):
    for j in range(w):
        print(ans[i][j], end = " ")
    print()