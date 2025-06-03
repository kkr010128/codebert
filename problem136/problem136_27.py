#
import sys
n = int(input())
#素因数分解
def factorization(n):
    arr = []
    tmp = n
    #2から√n でnを割る ･･･割れた回数を指数として追加
    for i in range(2, int(n ** 0.5 // 1) + 1):
        if tmp % i == 0:
            cnt = 0
            while tmp % i == 0:
                cnt += 1
                tmp //= i
            arr.append([i, cnt])
    if tmp != 1:  #割り切れなかったとき
        arr.append([tmp, 1])
    if arr == []: #素数の場合(割れなかった場合)
        arr.append([n, 1])
    return arr

p = factorization(n)
count = 0
#すべての素因数で分解する
for x in p:
    #割れなくなったら抜ける
    if n == 1:
        break
    #x[i][0]の１からp[i][1]乗で割る
    for j in range(1, x[1] + 1):
        if n % (x[0]**j) == 0:
            n /= x[0]**j
            count += 1
        else:#割れなくなったら抜ける
            break
print(count)