## H, Kの値が小さいので塗り方の全ての通りを調べる方針でよい(全探索)
## 各塗り方について全てのマスが黒いかどうか調べて、黒いマスがK個あればよい
## itertoolsモジュールを使ってみる
from itertools import product
H, W, K = (int(x) for x in input().split())
C = [list(input()) for _ in range(H)] #H行〇列の行列を格納する
answer = 0

for row_bit in product(range(2), repeat=H):
#"product(range(2), repeat=H)"で長さがHで、各要素が1か0であるすべての組み合わせがすべて列挙される.
## cf.) https://docs.python.org/ja/3/library/itertools.html#itertools.product
    for col_bit in product(range(2), repeat=W):
        cnt = 0
        for row in range(H):
            for col in range(W):
                if C[row][col] == "#" and (row_bit[row] and col_bit[col]):
                    cnt += 1
        if cnt == K:
            answer += 1
print(answer)
## 参考 : https://qiita.com/u2dayo/items/90a0693f31524e7b4cd0#c%E5%95%8F%E9%A1%8Ch-and-v
