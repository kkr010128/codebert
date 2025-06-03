#!/usr/bin/env python3
h,w,k = map(int,input().split())
b =[]
for i in range(h):
    s = input()
    b.append(s)
# 縦の切り方を固定すれば、左から見て貪欲に考えることができる。
# どれかの切り方でK+1　以上1 のマスがあれば、そこで切る
if h == 1:
    print(math.ceil(s//k))
    exit()
# リストで現在のそれぞれのブロックの1の数を持つ

# 列の切断が入ったときに全て0に初期化
# bit 全探索は 2 ** h-1 存在する 
ans = h*w #INF
for i in range(2**(h-1)):
    cnt_white = [0] 
    # ループの中で宣言する
    ans_i = 0
    #前処理として、どこに切れ込みがあるかを見て、リストの構成
    for bit in range(h-1):
        if i >> bit & 1:
            cnt_white.append(0)
            ans_i += 1
    #print("i = ",i,cnt_white)
    c = 0
    last_div = 0
    while c < w:# 左から貪欲
        r_idx = 0
        
        for r in range(h):
            if b[r][c] == "1":#対応するブロックのcnt+=1
                cnt_white[r_idx] += 1
                #print("col = ",c,cnt_white,r_idx,ans_i)
            if i >> r & 1:#次にブロックが変わるのでidxを増やす
                r_idx += 1
        # 1行だけでmax(cnt_white) >= k+1になるときはその切り方では不可能
        if max(cnt_white) >= k+1:
            # 戻らないといけない
            ans_i += 1
            if c == last_div:
                ans_i = h*w  #INF
                break
            last_div = c
            c -= 1
            cnt_white = [0]*len(cnt_white)#初期化
            #print("initialize",last_div)
        c += 1
    ans = min(ans,ans_i)
print(ans)