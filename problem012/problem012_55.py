import math
cnt = 0
for i in range(int(input())):
    x = int(input())
    flg = False # なんらかの数で割り切れるかどうか
    if x == 1:
        continue
    if x == 2:
        cnt += 1
        continue
    for k in range(2, math.floor(math.sqrt(x))+1):
        if not(x % k):
            flg = True
            break
    if not flg:
        cnt += 1
print(cnt)
