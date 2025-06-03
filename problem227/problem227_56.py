

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    N, K = read_ints()
    H = read_ints()
    if K >= N:
        return 0
    H.sort(reverse=True)
    return sum(H[K:])


if __name__ == '__main__':
    print(solve())
