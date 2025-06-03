h, w, k = map(int, input().split())
tbl = [input() for _ in range(h)]

# ビット全探索で全パターンをチェック
# n個のものからいくつか選ぶ組み合わせの数は 2**n 
# 例えば、3個の場合は 2**3 = 8通り
# 0: 0b000
# 1: 0b001
# 2: 0b010
# 3: 0b011
# 4: 0b100
# 5: 0b101
# 6: 0b110
# 7: 0b111
# バイナリの 0 は選ばれている、1 は選ばれていない
# https://drken1215.hatenablog.com/entry/2019/12/14/171657
ans = 0
for i in range(2**h):
    for j in range(2**w):
        ct = 0
        for ii in range(h):
            for jj in range(w):
                # 塗りつぶされない黒をカウントする
                # カウントした結果が残った数と同じであれば、回答に+1
                if (i>>ii)&1 == 0 and (j>>jj)&1 == 0:
                    if tbl[ii][jj] == '#':
                        ct += 1
        if ct == k:
            ans += 1
print(ans)
                    
