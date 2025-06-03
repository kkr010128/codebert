def shuffle(str, m):
    return str[m:] + str[0:m]

if __name__ == '__main__':
    while True:
        str = input()
        if str == '-':
            break
        m = int(input())
        for _ in range(m):
            str = shuffle(str, int(input()))

        print(str)
