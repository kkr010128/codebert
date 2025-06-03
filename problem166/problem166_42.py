def main():
    s = input()
    mod = 2019
    mod_count = {i: 0 for i in range(mod)}
    now_num = 0
    base = 1
    for i in range(len(s) - 1, -1, -1):
        mod_count[now_num] += 1
        now_num += base * int(s[i])
        now_num %= mod
        base *= 10
        base %= mod
    ans = 0
    mod_count[now_num % mod] += 1
    for i in range(mod):
        ans += mod_count[i] * (mod_count[i] - 1) // 2
    print(ans)


if __name__ == '__main__':
    main()

