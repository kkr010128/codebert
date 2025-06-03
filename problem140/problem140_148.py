def main():
    t = input()
    ans = ''
    for c in t:
        if c == '?':
            ans += 'D'
        else:
            ans += c
    print(ans)


if __name__ == '__main__':
    main()
