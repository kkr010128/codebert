import itertools as itr

def call(n):
    def devided_3(x):
        return x % 3 == 0

    def has_3(x):
        return '3' in str(x)

    data = filter(lambda x: devided_3(x) or has_3(x), range(1, n+1))
    [print(' {0}'.format(i), end='') for i in data]
    print()

if __name__ == '__main__':
    n = int(input())
    call(n)