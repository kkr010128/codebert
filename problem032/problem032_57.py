import math

n = int(input())
x_lst = map(int, input().split())
y_lst = map(int, input().split())

xy_lst = list(zip(x_lst, y_lst))

p1 = 0
p2 = 0
p3 = 0
p4 = []
for x, y in xy_lst:
    # マンハッタン距離
    p1 += abs(x - y)
    # ユークリッド距離
    p2 += (abs(x - y)) ** 2
    p3 += (abs(x - y)) ** 3
    # チェビシェフ距離
    p4.append(abs(x - y))
print(p1)
print(math.sqrt(p2))
print(math.pow(p3, 1 / 3))
print(max(p4))
