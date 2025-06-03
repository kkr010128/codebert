def search(n):
    res = 0
    while n:
        n %= bin(n).count("1")
        res += 1
    return res


def main():
    n = int(input())
    x = list(input())
    x_decimal = int("".join(map(str, x)), 2)
    first_mod = sum(map(int, list(x)))
    increase_mod = first_mod + 1
    increase_base = x_decimal % increase_mod  # 反転させる桁が元々0だった場合
    decrease_mod = first_mod - 1
    if decrease_mod:
        decrease_base = x_decimal % decrease_mod  # 反転させる桁が元々1だった場合
    for i in range(n):
        cnt = 0
        if x[i] == "1" and decrease_mod:
            cnt = 1 + search((decrease_base - pow(2, n - i - 1, decrease_mod)) % decrease_mod)
        elif x[i] == "0":
            cnt = 1 + search((increase_base + pow(2, n - i - 1, increase_mod)) % increase_mod)
        print(cnt)


if __name__ == '__main__':
    main()

