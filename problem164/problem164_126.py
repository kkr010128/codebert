import math

A, B, C, D = map(int, input().split())

#何ターンで倒せるかを比較、ターン数が小さい方が強い。ターン数が同じなら高橋が勝ち。

if math.ceil(C / B) <= math.ceil(A / D):
    print("Yes")
else:
    print("No")