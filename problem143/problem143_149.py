def main():
    k = int(input())
    s = str(input())

    output = ''
    if len(s) > k:
        for i in range(k):
            output += s[i]
        output += '...'
    else:
        output = s

    print(output)


if __name__ == '__main__':
    main()