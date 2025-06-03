import math
x = int(input())
def isPrime(num):
    # 2未満の数字は素数ではない
    if num < 2: return False
    
    # 3 ~ numまでループし、途中で割り切れる数があるか検索
    # 途中で割り切れる場合は素数ではない
    for i in range(2, math.floor(math.sqrt(num))+1):
        if num % i == 0:
            return False
    # 素数
    return True
  
for i in range(x, 10**6):
    if isPrime(i):
        print(i)
        break
