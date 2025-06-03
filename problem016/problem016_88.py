def selection_sort(numbers, n, key=lambda x: x):
    """selection sort method

    Args:
        numbers: a list of numbers to be sorted
        n: len(numbers)
        key: sort key

    Returns:
        sorted numberd, number of swapped times
    """
    x = []
    for data in numbers:
        x.append(data)

    counter = 0

    for i in range(0, n):
        min_j = i
        for j in range(i, n):
            if key(x[j]) < key(x[min_j]):
                min_j = j
        if min_j != i:
            x[min_j], x[i] = x[i], x[min_j]
            counter += 1
    return x, counter


def bubble_sort(numbers, n, key=lambda x: x):
    """bubble sort method

    Args:
        numbers: a list of numbers to be sorted by bubble sort
        n: len(list)
        key: sort key

    Returns:
        sorted list
    """
    x = []
    for data in numbers:
        x.append(data)

    flag = True
    counter = 0
    while flag:
        flag = False
        for index in range(n - 1, 0, -1):
            if key(x[index]) < key(x[index - 1]):
                x[index], x[index - 1] = x[index - 1], x[index]
                flag = True
                counter += 1
    return x, counter


def insertion_sort(numbers, n, key=lambda x: x):
    """insertion sort method

    Args:
        numbers: a list of numbers to be sorted
        n: len(numbers)

    Returns:
        sorted list
    """
    for i in range(1, n):
        target = numbers[i]
        index = i - 1
        while index >= 0 and target < numbers[index]:
            numbers[index + 1] = numbers[index]
            index -= 1
        numbers[index + 1] = target

    return numbers


def is_stable(list1, list2):
    """check stablity of sorting method used in list2

    Args:
        list1: sorted list(bubble sort)
        list2: sorted list(some sort)

    Returns:
        bool
    """
    flag = True
    for index, data in enumerate(list1):
        if list2[index] != data:
            flag = False
            break

    return flag


length = int(raw_input())
cards = raw_input().split()
bubble_sorted_card, bubble_swapped = bubble_sort(numbers=cards, n=length, key=lambda x: int(x[1]))
selection_sorted_card, selection_swapped = selection_sort(numbers=cards, n=length, key=lambda x: int(x[1]))
print(" ".join(bubble_sorted_card))
print("Stable")
print(" ".join(selection_sorted_card))

if is_stable(bubble_sorted_card, selection_sorted_card):
    print("Stable")
else:
    print("Not stable")