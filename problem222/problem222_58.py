

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    N = read_int()
    A = read_ints()
    if len(A) == len(set(A)):
        return 'YES'
    return 'NO'


if __name__ == '__main__':
    print(solve())
