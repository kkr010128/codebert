h, w, k = map(int, input().split())
s = [[int(i) for i in input()] for _ in range(h)]
ans = (h-1)+(w-1)
for i in range(2**(h-1)):
    d = [(i >> j) & 1 for j in range(h-1)]
    count, count_tmp = [0]*(sum(d)+1), [0]*(sum(d)+1)
    ans_, res = 0, 0
    flag = False
    for w_ in range(w):
        count[0] += s[0][w_]
        count_tmp[0] += s[0][w_]
        res += 1
        tmp = 0
        for h_ in range(1, h):
            if d[h_-1]: tmp += 1
            if s[h_][w_]:
                count[tmp] += 1
                count_tmp[tmp] += 1
        for j in count:
            if j > k:
                if res==1:
                    flag = True
                    break
                else:
                    for idx in range(sum(d)+1):
                        count[idx] = count_tmp[idx]
                    ans_ += 1
                    res = 1
                    break
        if flag: break
        count_tmp = [0]*(sum(d)+1)
    if flag: continue
    ans_ += sum(d)
    ans = min(ans, ans_)
print(ans)