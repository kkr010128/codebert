def main():
    s = input()
    n = len(s)

    rule1 = True
    rule2 = True
    rule3 = True

    for i in range(n):
        if s[i] != s[n - 1 - i]:
            rule1 = False
            break

    for i in range(n // 2):
        if s[i] != s[n // 2 - 1 - i]:
            rule2 = False
            break

    for i in range(n // 2):
        if s[n // 2 + 1 + i] != s[n - 1 - i]:
            rule3 = False
            break

    if rule1 and rule2 and rule3:
        ans = "Yes"
    else:
        ans = "No"

    print(ans)


if __name__ == "__main__":
    main()
