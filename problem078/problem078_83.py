def main():
    N = int(input())
    mod = 10 ** 9 + 7
    mod_1 = 1
    mod_2 = 1
    mod_3 = 1
    for _ in range(N):
        mod_1 = (mod_1 * 10) % mod
        mod_2 = (mod_2 * 9) % mod
        mod_3 = (mod_3 * 8) % mod
    v = (mod_1 - 2 * mod_2 + mod_3) % mod
    print(v)

if __name__ == '__main__':
    main()