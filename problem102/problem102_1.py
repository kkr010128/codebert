def main():
    N, K = input_ints()
    A = input_int_list_in_line()

    for i in range(N-K):
        if A[i] < A[i+K]:
            print('Yes')
        else:
            print('No')


def input_ints():
    line_list = input().split()

    if len(line_list) == 1:
        return int(line_list[0])
    else:
        return map(int, line_list)


def input_int_list_in_line():
    return list(map(int, input().split()))


def input_int_tuple_list(n: int):
    return [tuple(map(int, input().split())) for _ in range(n)]


main()
