def main():
    s = input()
    t = input()
    ans = 0
    for i, char in enumerate(s):
        if char != t[i]:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
