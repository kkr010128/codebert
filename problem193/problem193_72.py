import copy

h, w, k = map(int, input().split())
s = [[0] * w for _ in range(h)]
for i in range(h):
    inp = input()
    for j in range(w):
        s[i][j] = int(inp[j])

# 最終的に出力する操作回数の最小値
ans = h + w - 2

for i in range(2 ** (h-1)):
    # bit全探索によるcutの仕方
    cutIdx = [0] * (h-1)
    for j in range(h-1):
        cutIdx[j] = (i >> j) & 1
    #print('cI : ', cutIdx)

    # cutする場所を示したリスト
    div = []
    cut_row_begin, cut_row_end = 0, 1
    for j in range(h-1):
        if cutIdx[j] == 0:
            # cutしない
            cut_row_end += 1
        else:
            # cutする
            div.append((cut_row_begin, cut_row_end))
            cut_row_begin = cut_row_end
            cut_row_end += 1
    div.append((cut_row_begin, cut_row_end))
    #print('div: ', div)

    # 既にここまででcutされている回数
    cnt = sum(cutIdx)
    #print(cnt)

    # divごとのホワイトチョコの数をカウント
    whiteCnt = [0] * len(div)

    # まずは1列目をチェック
    for a in range(len(div)):
        cal = 0
        for b in range(div[a][0], div[a][1]):
            cal += s[b][0]
        whiteCnt[a] = cal
    #print('wC : ', whiteCnt)

    # もしこの時点でwhiteCntの要素でkを超えるものがあるとき
    # その横の切り方は不可能なのでbreak
    if max(whiteCnt) > k:
        continue

    # Wが1ならそこで終わり
    if w == 1:
        ans = min(ans, cnt)

    # 次行のホワイトチョコ数を保持
    search = [0] * len(div)

    # 2列目以降を同様にチェックしていく
    for a in range(1, w):
        # その次行のホワイトチョコの数
        for b in range(len(div)):
            cal = 0
            for c in range(div[b][0], div[b][1]):
                cal += s[c][a]
            search[b] = cal

        # その行単体でmax値とkを比べる
        # オーバーしていればcut不可
        if max(search) > k:
            break

        # greedy
        for b in range(len(div)):
            if whiteCnt[b] + search[b] > k:
                # cut対象
                cnt += 1
                whiteCnt = copy.copy(search)
                break
            else:
                whiteCnt[b] += search[b]
    #print('cnt: ', cnt)
    ans = min(ans, cnt)

print(ans)