
def main():
    s = list(input())
    k = int(input())
    lst = []
    cnt = 1
    flg = 0
    ans = 0
    prev = s[0]
    for i in range(1, len(s)):
        if prev == s[i]:
            cnt += 1
        else:
            lst.append(cnt)
            cnt = 1
            prev = s[i]
            flg = 1
    lst.append(cnt)
    if len(lst) == 1:
        ans = len(s) * k // 2
    else:
        ans += sum(map(lambda x: x // 2, lst[1:len(lst)-1])) * k
        # for l in lst[1: len(lst) - 1]:
        #     ans += l // 2 * k
        if s[-1] == s[0]:
            ans += (lst[0] + lst[-1]) // 2 * (k - 1)
            ans += lst[0] // 2 + lst[-1] // 2
        else:
            ans += (lst[0] // 2 + lst[-1] // 2) * k
    print(ans)


if __name__ == "__main__":
    main()
