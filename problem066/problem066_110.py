def shuffle(s,n):
    if len(s) <= 1:
        return s
    ans = s[n:] + s[:n]
    return ans


def main():
    while True:
        strings = input()
        if strings == "-":
            break
        n = int(input())
        li = []
        for i in range(n):
            li.append(int(input()))
        for i in li:
            strings = shuffle(strings, i)
        print(strings)


if __name__ == "__main__":
    main()