def main():
    n = int(input())
    s = [list(input()) for _ in range(n)]
    L_cnt = []
    R_cnt = []
    LR_cnt = []
    min_l,min_r = 10**6,10**6
    for i in range(n):
        t = s[i]
        flag = 0
        l = 0
        r = 0
        for j in range(len(t)):
            if not flag and t[j] == ')':
                r += 1
            elif t[j] == '(':
                flag = 1
                l += 1
            else:
                l -= 1
                if l == 0:
                    flag = 0
        if r == 0 and l == 0:
            continue
        if r == 0:
            L_cnt.append(l)
        elif l == 0:
            R_cnt.append(r)
        else:
            LR_cnt.append([l,r])
            min_l = min(min_l,l)
            min_r = min(min_r,r)
    L,R = sum(L_cnt),sum(R_cnt)
    if not LR_cnt:
        if L == R:
            print('Yes')
            return
        else:
            print('No')
            return
    if not (L_cnt and R_cnt):
        print('No')
        return
    box1 = []
    box2 = []
    for i in range(len(LR_cnt)):
        if L >= LR_cnt[i][1] and LR_cnt[i][1] <= LR_cnt[i][0]:
            L += LR_cnt[i][0] - LR_cnt[i][1]
        elif LR_cnt[i][1] <= LR_cnt[i][0]:
            box1.append(LR_cnt[i])
        else:
            box2.append(LR_cnt[i])
    for i in range(len(box1)):
        L -= box1[i][1]
        if L < 0:
            print('No')
            return
        L += box1[i][0]
    for i in range(len(box2)):
        L -= box2[i][1]
        if L < 0:
            print('No')
            return
        L += box2[i][0]
    if L == R:
        print('Yes')
    else:
        print('No')
    
if __name__ == "__main__":
    main()