def input_number():
    num = raw_input()
    array = num.strip().split(" ")
    int_array = map(int, array)

    return int_array


def main():
    n = raw_input()
    count = 0
    int_array = input_number()
    for i in range(int(n)):
        minj = i
        for j in range(i, int(n)):
            if int_array[j] < int_array[minj]:
                minj = j
        v = int_array[i]
        int_array[i] = int_array[minj]
        int_array[minj] = v
        if minj != i:
            count += 1
    array = map(str, int_array)
    print " ".join(array)
    print count


if __name__ == '__main__':
    main()