#!usr/bin/env python3

def string_two_numbers_spliter():
    a, b, c = [int(i) for i in input().split()]
    return a, b, c


def count_nums_of_divisors_of_c_in_a_and_b(a, b, c):
    count = 0
    for i in range(1, c+1):
        if (c % i == 0):
            if i >= a and i <= b:
                count += 1
    return count


def main():
    a, b, c = string_two_numbers_spliter()
    print(count_nums_of_divisors_of_c_in_a_and_b(a, b, c))


if __name__ == '__main__':
    main()