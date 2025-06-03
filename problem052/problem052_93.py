if __name__ == '__main__':
    limit = int(input())

    data = []
    for i in range(3, limit+1):
        if (i % 3) == 0 or '3' in str(i):
            data.append(str(i))

    txt = ' '.join(data)
    print(' {0}'.format(txt))