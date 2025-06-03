h , w , k = map(int,input().split())
cho = [list(input()) for i in range(h)]
ans = 10**9
for i in range(2**(h-1)):
    cut = [0 for i in range(h)]
    for j in range(h-1):
        if i >> j & 1 == 1:
            cut[j+1] = cut[j]+1
        else:
            cut[j+1] = cut[j]
    maxcut = max(cut)+1
    cou = [0 for i in range(maxcut)]
    ccho = [[0 for i in range(w)] for j in range(maxcut)]
    for j in range(h):
        for l in range(w):
            ccho[cut[j]][l] += int(cho[j][l])
    tyu = maxcut - 1
    hukanou = False
    for j in range(w):
        flag = True
        for l in range(maxcut):
            if cou[l] + ccho[l][j] > k:
                flag = False
                break
        if flag:
            for l in range(maxcut):
                cou[l] += ccho[l][j]
        elif not flag:
            tyu += 1
            for l in range(maxcut):
                if ccho[l][j] > k:
                    hukanou = True
                    break
                cou[l] = ccho[l][j]
        if hukanou:
            break
    if hukanou:
        continue
    ans = min(ans,tyu)
print(ans)