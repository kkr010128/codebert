import sys
x = int(input())
import math

# 素数判定関数
def isPrime(num):
    # 2未満の数字は素数ではない
    if num < 2: return False
    # 2は素数
    elif num == 2: return True
    # 偶数は素数ではない
    elif num % 2 == 0: return False

    # 3 ~ numまでループし、途中で割り切れる数があるか検索
    # 途中で割り切れる場合は素数ではない
    for i in range(3, math.floor(math.sqrt(num))+1, 2):
        if num % i == 0:
            return False

    # 素数
    return True

# 素数判定
def callIsPrime(input_num=1000):
    numbers = []
    # ループしながら素数を検索する
    for i in range(1, input_num):
        if isPrime(i):
            numbers.append(i)

    # 素数配列を返す
    return numbers

# 関数の呼び出し
# print(callIsPrime(100000+4)[-1])

for i in callIsPrime(100000+4):
    if i>=x:
        print(i)
        sys.exit()