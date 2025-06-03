def main():
    n = int(input())
    # n, k = map(int, input().split())
    # h = list(map(int, input().split()))
    s = input()

    ans = ""

    for i in s:
        ans += chr((ord(i) - ord("A") + n)% 26 + ord("A"))

    print(ans)


if __name__ == '__main__':
    main()
