def main():
    N = int(input())
    # 桁数を求める
    n_digit = 0
    idx = 0
    while True:
        n_digit += 1
        n_str = 26 ** n_digit
        if idx + 1 <= N <= idx + n_str:
            idx += 1
            break
        else:
            idx += n_str

    k = N - idx
    ans = ''
    for i in range(n_digit):
        ans += chr(ord('a') + k % 26)
        k //= 26
    print(ans[::-1])


if __name__ == '__main__':
    main()
