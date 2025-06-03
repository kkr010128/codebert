def substring(s, t):
    min = 10000    # 変更数の最小
    startIdx = 0   # arraySのstartインデックス
    arrayIdx = 0   # arraySのインデックス
    arrayS = []
    arrayT = []
    
    for item in s:
        arrayS.append(item)

    # Sの文字列-Tの文字列+1回ループ
    loopCnt = len(s) - len(t) + 1
    for i in range(0, loopCnt):
        count = 0       # 変更数

        arrayIdx = startIdx

        for item in t:
            if not item == arrayS[arrayIdx]:
                count += 1
            arrayIdx += 1

        if count < min:
            min = count
        
        startIdx += 1

    print(min)


        

s = input()
t = input()

substring(s, t)