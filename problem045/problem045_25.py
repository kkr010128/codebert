if __name__ == '__main__':
    key_in = input()
    data = [int(x) for x in key_in.split(' ')]
    a = data[0]
    b = data[1]

    print('{0} {1} {2:.5f}'.format(a//b, a%b, a/b))