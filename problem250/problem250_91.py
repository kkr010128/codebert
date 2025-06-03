import math
X = int(input())
X -= 1

while True:
    flg = 0
    X += 1
    lim = int(math.sqrt(X))
    for i in range(2, lim+1):
        if X % i == 0:
            flg = 1
            break
    if flg == 1:
        continue
    break
print(X)