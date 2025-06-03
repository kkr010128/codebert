from math import ceil
from fractions import gcd

N, M = map(int, input().split())
A = list(map(int, input().split()))

# 2で割ったものに置き換え
A = [a // 2 for a in A]


def lcm(x, y):
    return x*(y//gcd(x, y))


# 各要素について、2で割り切れる回数が等しいかチェック
count_div_2 = None
for a in A:
    cnt = 0
    while a % 2 == 0:
        a //= 2
        cnt += 1

    if count_div_2 is None:
        count_div_2 = cnt
    elif cnt != count_div_2:
        print(0)
        exit()

# LCM計算
while len(A) > 1:
    a, b = A.pop(), A.pop()
    my_lcm = lcm(a, b)

    # Mを超えたlcmは意味がない
    if my_lcm > M:
        print(0)
        exit()

    A.append(my_lcm)


print(ceil(M // A[0] / 2))
