def input_data():
    num = raw_input()
    array = []
    array = num.strip().split(" ")
    array = map(int, array)
    return array


def main():
    n = raw_input()
    count = 0
    array = input_data()
    flag = True
    i = 0
    while flag:
        flag = False
        for j in reversed(xrange(i + 1, int(n))):
            if array[j] < array[j - 1]:
                v = array[j]
                array[j] = array[j - 1]
                array[j - 1] = v
                flag = True
                count += 1
        i += 1
    array = map(str, array)
    print " ".join(array)
    print str(count)


if __name__ == '__main__':
    main()