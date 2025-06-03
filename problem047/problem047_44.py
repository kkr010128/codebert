if __name__ == '__main__':

    while True:
        key_in = input()
        data = key_in.split(' ')

        a = int(data[0])
        op = data[1]
        b = int(data[2])

        if op == '+':
            print('{0}'.format(a + b))
        if op == '-':
            print('{0}'.format(a - b))
        if op == '*':
            print('{0}'.format(a * b))
        if op == '/':
            print('{0}'.format(a // b))
        if op == '?':
            break