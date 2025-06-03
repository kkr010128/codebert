h,w,k = map(int, input().split())
s = [[int(c) for c in input()] for i in range(h)]
ans = 114514893
for bit in range(1 << (h-1)):
    cut = [-1]
    for i in range(h-1):
        if bit & (1 << i) : cut.append(i)
    cut.append(h-1)
    l = len(cut)-1
    count = l-1
    suml = [0 for i in range(l)]
    ok = True
    for i in range(w):
        sumtemp = [0 for ii in range(l)]
        flag2 = True #kを超えないかどうか
        for j in range(l):
            for kk in range(cut[j]+1,cut[j+1]+1):
                sumtemp[j] = sumtemp[j] + s[kk][i]
            if sumtemp[j] > k:
                ok = False
                break
        if not ok : break
        for j in range(l):
            if suml[j]+sumtemp[j] > k:flag2 = False
        if flag2:
            for j in range(l):
                suml[j] = suml[j]+sumtemp[j]
        else:
            count += 1
            suml = sumtemp[:]   
    if not ok:continue
    ans = min(ans,count)
    
print(ans)