#D 素数の公約数-> 素因数分解で共通な素因数を求めて個数を入力
import sys
a, b = map(int, input().split())

#素因数分解(2以降)
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

a = factorization(a)
b = factorization(b)
ans = 1
# print(a, b)
if a[0][0] == b[0][0] == 1:
    print(ans)
    sys.exit()
for i in a:
    for j in b:
        if i[0] == j[0]:
            ans += 1
print(ans)