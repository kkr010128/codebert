import itertools


n, m, q = map(int, input().split())
pairs = []
for i in range(q):
    pairs.append(list(map(int, input().split())))

elem = [i for i in range(1, m+1)]

# elemからn回くじを引いて，出た値を昇順にソートする．引いたくじはすぐにelemに戻す．この全組み合わせをリストで返す．
candidates = list(itertools.combinations_with_replacement(elem, n))

dsummax = 0
for cand in candidates:
    dsum = 0
    for i in range(q):
        if cand[pairs[i][1]-1]-cand[pairs[i][0]-1] == pairs[i][2]:
            dsum += pairs[i][3]
    if dsummax < dsum:
        dsummax = dsum

print(dsummax)
