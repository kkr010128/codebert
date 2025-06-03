S = input()
K = int(input())

#ランレングス圧縮
rle = []
pre = 'A'
chain = 1
for c in S:
    if c == pre:
        chain += 1
    else:
        if pre != 'A':
            rle.append([pre,chain])
        
        pre = c
        chain = 1
rle.append([pre,chain])

ans = 0

#1種類の文字列の場合
if len(rle) == 1:
    ans = (rle[0][1] * K) // 2

#2種類以上の文字列の場合
else:
    #先頭と末尾が同じ文字
    if rle[0][0] == rle[-1][0]:
        #先頭、末尾、つなぎ目の対応
        ans += rle[0][1]//2
        ans += rle[-1][1]//2
        rle[0][1] += rle[-1][1]
        rle[-1][1] = 0
        ans += rle[0][1]//2 * (K-1)

        #Sの中での連続文字の対応
        mid_chains = 0
        for i in range(1,len(rle)):
            mid_chains += rle[i][1]//2
        ans += mid_chains * K

    #先頭と末尾が異なる文字
    else:
        mid_chains = 0
        for i in range(len(rle)):
            mid_chains += rle[i][1]//2
        ans += mid_chains * K


#print(rle)
print(ans)