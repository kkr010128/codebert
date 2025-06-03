def show(array):
    for i in range(len(array)):
        if i != len(array) - 1:
            print(array[i], end=' ')
        else:
            print(array[i])


def bubbleSort(array):
    flag = True
    count = 0
    while flag:
        flag = False
        for j in sorted(range(1, len(array)), reverse=True):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = [array[j - 1], array[j]]
                flag = True
                count += 1
    show(array)
    return count


input()
array = [int(x) for x in input().split()]

print(bubbleSort(array))

