def main():
    N = int(input())
    ans = 0
    for n in range(1,  N + 1):
        d = N // n
        ans += d * (d + 1) / 2 * n
    print(int(ans))

if __name__ == '__main__':
    main()