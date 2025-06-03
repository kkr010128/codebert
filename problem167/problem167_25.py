import math

def main():

    R = input_int()

    print(R * 2 * math.pi)


def input_int():
    return int(input())


def input_ints():
    return map(int, input().split())


def input_int_list_in_line():
    return list(map(int, input().split()))


def input_int_tuple_list(n: int, q: int):
    return [tuple(map(int, input().split())) for _ in range(n)]


main()
