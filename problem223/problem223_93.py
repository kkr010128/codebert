

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    """
    1 2
    /2 = 1.5

    1 2 3 4
    /4 = 2.5

    1 2 3 4 5
    /5 = 3
    """
    N, K = read_ints()
    expectations = [(p+1)/2 for p in read_ints()]
    max_e = current = sum(expectations[:K])
    for i in range(1, N-K+1):
        # remove i-1 add i+K
        current = current-expectations[i-1]+expectations[i+K-1]
        max_e = max(max_e, current)
    return max_e


if __name__ == '__main__':
    print(solve())
