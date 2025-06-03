import math

A, B, C, D = map(int, input().split())

T_kougeki = C / B     # 高橋くんが攻撃して、青木くんの体力が0になるまでの回数
A_kougeki = A / D     # 青木くんが攻撃して、高橋くんの体力0になるまでの回数

if math.ceil(T_kougeki) <= math.ceil(A_kougeki):   #切り上げた値で少ない方、同数なら先行の高橋くんの勝ち
    print('Yes')

else:
    print('No')