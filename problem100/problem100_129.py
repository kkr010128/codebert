import copy

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
def get_int_multi():  # a, b = get_int_multi()
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

    m = get_int()
    ret = 0
    if m < 600:
        ret = 8
    elif m < 800:
        ret = 7
    elif m < 1000:
        ret = 6
    elif m < 1200:
        ret = 5
    elif m < 1400:
        ret = 4
    elif m < 1600:
        ret = 3
    elif m < 1800:
        ret = 2
    elif m < 2000:
        ret = 1

    print(ret)




if __name__ == '__main__':
    main()


