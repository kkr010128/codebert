def main():
    L, R, d = input_ints()

    print(len([True for i in range(L, R+1) if i % d == 0]))




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
