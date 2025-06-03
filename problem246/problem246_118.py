import copy
import math
import time
import statistics
import math
import itertools

# a = get_int()
def get_int():
    return int(input())
# a = get_string()
def get_string():
    return input()
# a_list = get_int_list()
def get_int_list():
    return [int(x) for x in input().split()]
# a_list = get_string_list():
def get_string_list():
    return input().split()
# a, b = get_int_multi()
def get_int_multi():
    return map(int, input().split())
# a_list = get_string_char_list()
def get_string_char_list():
    return list(str(input()))
# print("{} {}".format(a, b))
# for num in range(0, a):
# a_list[idx]
# a_list = [0] * a
'''
while (idx < n) and ():

    idx += 1
'''

def main():
    start = time.time()
    n = get_int()
    p = get_int_list()
    q = get_int_list()

    a = []
    for i in range(1, n+1):
        a.append(i)

    count = 0
    count_p = 0
    count_q = 0
    for keiro in list(itertools.permutations(a)):
        if list(keiro) == p:
            count_p = count
        if list(keiro) == q:
            count_q = count
        count += 1

    print(abs(count_p - count_q))


if __name__ == '__main__':
    main()


