

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    S = input().strip()
    if S[2] == S[3] and S[4] == S[5]:
        return 'Yes'
    return 'No'


if __name__ == '__main__':
    print(solve())
