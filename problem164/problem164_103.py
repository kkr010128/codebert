# 高橋くんのモンスターは体力Aで攻撃力B
# 青木くんのモンスターは体力Cで攻撃力D
# 高橋くんが勝つならYes、負けるならNoを出力する

A, B, C, D = map(int, input().split())

while A > 0 and C > 0:
    C -= B
    A -= D

if C <= 0:
    print('Yes')
elif A <= 0:
    print('No')
