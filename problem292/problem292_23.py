

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    N = read_int()
    D = read_ints()
    S = sum(D)
    answer = 0
    for d in D:
        S -= d
        answer += d*S
    return answer


if __name__ == '__main__':
    print(solve())
