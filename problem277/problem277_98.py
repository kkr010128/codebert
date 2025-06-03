h,w,k = map(int, input().split())
cake = [input() for i in range(h)]
ans = [[0]*w for i in range(h)]

now = 1
for i in range(h):
    for j in range(w):
        if cake[i][j] == '#':
            ans[i][j] = now
            now+=1

for i in range(h):
    for j in range(1,w):
        if ans[i][j] == 0:
            ans[i][j] = ans[i][j-1]

for i in range(h):
    for j in reversed(range(w-1)):
        if ans[i][j] == 0:
            ans[i][j] = ans[i][j+1]

for i in range(1,h):
    for j in range(w):
        if ans[i][j] == 0:
            ans[i][j] = ans[i-1][j]

for i in reversed(range(h-1)):
    for j in range(w):
        if ans[i][j] == 0:
            ans[i][j] = ans[i+1][j]

for i in range(h):
    for j in range(w):
        print(ans[i][j], end=' ')
    print()