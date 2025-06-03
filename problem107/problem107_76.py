import sys

def popcount(x):
    '''xの立っているビット数をカウントする関数
    (xは64bit整数)'''

    # 2bitごとの組に分け、立っているビット数を2bitで表現する
    x = x - ((x >> 1) & 0x5555555555555555)

    # 4bit整数に 上位2bit + 下位2bit を計算した値を入れる
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)

    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f # 8bitごと
    x = x + (x >> 8) # 16bitごと
    x = x + (x >> 16) # 32bitごと
    x = x + (x >> 32) # 64bitごと = 全部の合計
    return x & 0x0000007f 

input = sys.stdin.readline
N = int(input())
X = input().strip()

n0 = 0
for x_i in X:
    if x_i == "1":
        n0 += 1
# print("n0", n0)
r_p = 0 # 0 -> 1のケース
r_n = 0 # 1 -> 0のケース
X = X[::-1]
for i in range(N):
    x = int(X[i])
    r_p += x * pow(2, i, n0+1)
    r_p %= (n0+1)
    if 1 < n0:
        r_n += x * pow(2, i, n0-1)
        r_n %= (n0-1)
# print("r_p", r_p, "r_n", r_n)

ans = []
# print(n)
for i in range(N):
    count = 1
    diff = (1 if X[i] == "0"  else -1)
    # print("x_i", X[i], "diff", diff)
    n = n0 + diff
    if n == 0:
        ans.append(0)
        continue
    if diff == 1:
        r = r_p + (diff * pow(2, i, n))
        r %= n
    else:
        r = r_n + (diff * pow(2, i, n))
        r %= n
    # print("n", n, "r", r)
    n = r
    # print("n", n)
    while 0 < n:
        r = popcount(n)
        count += 1
        # print("n", n)
        if r == 0:
            break
        n = n % r
    ans.append(count)

for i in ans[::-1]:
    print(i)