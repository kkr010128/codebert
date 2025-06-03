

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    H, A = read_ints()
    return H//A + (1 if H%A != 0 else 0)


if __name__ == '__main__':
    print(solve())
