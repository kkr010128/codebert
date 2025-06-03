H, W, K = map(int, input().split())
s = ['' for i in range(H)]
for i in range(H):
    s[i] = input()
now = 1
ans = [[] for i in range(H)]
count = 0
flag = False
for i in range(H):
    gokei = s[i].count('#')
    shap = 0
    if gokei >= 1:
        flag = True
        for j in range(W):
            ans[i].append(now)
            if j == W-1:
                now += 1
            elif s[i][j] == '#' and shap < gokei-1:
                now += 1
                shap += 1
            elif s[i][j] == '#' and shap == gokei-1:
                shap += 1
    elif gokei == 0 and flag:
        ans[i] = ans[i-1]
    elif gokei == 0 and flag == False:
        count += 1
for i in range(count):
    ans[i] = ans[count]
for i in range(H):
    print(*ans[i])
