n = int(input())
chars = "Xabcdefghijklmnopqrstuvwxyz"  # x番目がほしいときにchars[x-1]としたくないので、chars[0]は使わないことにします

n_rem = n  # 入力を直接操作すると、もし後々必要になったときに面倒なので
res = ""

while True:
    x = n_rem % 26
    # 余りが0、つまりzの場合は、26にします
    if x == 0:
        x = 26
    res += chars[x]

    # xを引いて、26で割ります
    n_rem -= x

    # 0なら終了します
    if n_rem == 0:
        break

    n_rem //= 26

# 0桁目が先頭で、最後の桁が末尾になっているので、反転させます
print(res[::-1])
