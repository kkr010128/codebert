def insertion_sort(array, element_number):
    for i in range(element_number):
        v = array[i]
        j = i - 1

        while(j>=0 and array[j] > v):
            array[j+1] = array[j]
            j = j - 1

        array[j+1] = v

        for k in range(element_number):
            if k < element_number-1:
                print(str(array[k]) + ' ', end='')
            else:
                print(str(array[k]), end='')

        print('\n', end='')

def test():
    element_number = int(input())
    input_array = list(map(int, input().split()))

    insertion_sort(input_array, element_number)

if __name__ == '__main__':
    test()