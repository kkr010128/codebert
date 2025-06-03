h, w, z = map(int ,input().split())
s = []
for i in range(h):
    s.append(list(input()))
ans = int(1e9+7)


for i2 in range(2**(h-1)):
    d = [True] * (h-1)
    for j2 in range(h-1):
        if (i2 >> j2) & 1:
            d[j2] = False
    d.append(False)


    val = 0
    for i in range(len(d)-1):
        if d[i] == False:
            val += 1
    #print(val,d)
    l = []
    lis = []
    for i in range(h):
        l.append(i)
        if d[i] == False:
            lis.append(l)
            l = []

    flg2 = True#横がiのときにcnt2の要素がkを超えるとFalse
    flg = True#cntの要素がkを超えるとFalse
    cnt = [0] * len(lis)#全体での1の個数
    for i in range(w):
        cnt2 = [0] * len(lis)#iでの1の個数
        for j in range(len(lis)):
            for k in lis[j]:
                if s[k][i] == '1':#高さがkで横がiの時、
                    cnt[j] += 1#lis[j]を1たす
                    cnt2[j] += 1
            if cnt[j] > z:
                flg = False
            if cnt2[j] > z:
                flg2 = False
        if flg == False:
            for j in range(len(cnt)):
                cnt[j] = cnt2[j]
            flg = True
            val += 1
        #print(cnt,cnt2)
        #print(i,val)
    if flg2 == True:
        ans = min(ans,val)
    #print(val,d,lis,flg)
print(ans)
