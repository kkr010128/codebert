H, W, K = map(int, input().split())
S = [[f for f in input()]for _ in range(H)]
Ans = [[0] * W for _ in range(H)]
num = 1
Flag = True
first = -1
for i in range(H):
    flag = False
    for j in range(W):
        if (S[i][j] == '#') and flag:
            num += 1
        if (S[i][j] == '#') and Flag:
            first = i
        if S[i][j] == '#':
            flag = True
            Flag = False
        Ans[i][j] = num
    if not flag:
        Ans[i] = Ans[i-1]
    else:
        num += 1

while first > 0:
    Ans[first - 1] = Ans[first]
    first -= 1

for ans in Ans:
    for i, a in enumerate(ans):
        if i == W-1:
            print(a)
        else:
            print(a, end=' ')






