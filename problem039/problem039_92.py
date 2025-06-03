if __name__ == '__main__':
    key_in = input()
    data = key_in.split(' ')

    a = int(data[0])
    b = int(data[1])
    c = int(data[2])

    if a < b < c:
        print('Yes')
    else:
        print('No')