h, w, k = map(int, input().split())
S = [list(input()) for _ in range(h)]
ans = S.copy()

index = 1
for i in range(h):
    for j in range(w):
        if S[i][j] == "#":
            ans[i][j] = str(index)
            index += 1

for i in range(h):
    for j in range(w-1):
        if ans[i][j] != "." and ans[i][j+1] == ".":
            ans[i][j+1] = ans[i][j] 

for i in range(h):
    for j in range(w-1, 0, -1):
        if ans[i][j] != "." and ans[i][j-1] == ".":
            ans[i][j-1] = ans[i][j]

for j in range(w):
    for i in range(h-1):
        if ans[i][j] != "." and ans[i+1][j] == ".":
            ans[i+1][j] = ans[i][j]

for j in range(w):
    for i in range(h-1, 0, -1):
        if ans[i][j] != "." and ans[i-1][j] == ".":
            ans[i-1][j] = ans[i][j]

for l in ans:
    print(" ".join(l))