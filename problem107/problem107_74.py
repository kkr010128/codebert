from functools import lru_cache


def popcnt(x):
    return bin(x).count("1")


@lru_cache(maxsize=None)
def rec(n):
    if n == 0:
        return 0
    else:
        return rec(n % popcnt(n)) + 1


n = int(input())
arr = input()

ALL_ARR = int(arr, 2)

# ALL_ARR mod popcnt±1を予め計算しておく
cnt = popcnt(int(arr, 2))
init_big = ALL_ARR % (cnt + 1)
if cnt == 1:
    init_small = 0
else:
    init_small = ALL_ARR % (cnt - 1)

# 変更部分だけ調整して剰余を再計算する
# 調整部分だけでも数が大きいためpowの引数modで高速化
li = [0] * n
for i in range(n):
    if arr[i] == "0":
        li[i] = (init_big + pow(2, n - i - 1, cnt + 1)) % (cnt + 1)

    # 0除算回避のためにフラグを立てておく
    elif ALL_ARR - (1 << (n - i - 1)) == 0 or cnt - 1 == 0:
        li[i] = "flg"
    else:
        li[i] = (init_small - pow(2, n - i - 1, cnt - 1)) % (cnt - 1)

ans = []

for x in li:
    if x == "flg":
        ans.append(0)
    else:
        ans.append(rec(x) + 1)

print(*ans, sep="\n")