def selection_sort(numbers, n):
    """selection sort method

    Args:
        numbers: a list of numbers to be sorted
        n: len(numbers)

    Returns:
        sorted numberd, number of swapped times
    """
    counter = 0
    for i in range(0, n - 1):
        min_j = i
        for j in range(i + 1, n):
            if numbers[j] < numbers[min_j]:
                min_j = j
        if min_j != i:
            numbers[min_j], numbers[i] = numbers[i], numbers[min_j]
            counter += 1
    return numbers, counter


length = int(raw_input())
numbers = [int(x) for x in raw_input().split()]

numbers, number_of_swapped_times = selection_sort(numbers, length)
print(" ".join([str(x) for x in numbers]))
print(number_of_swapped_times)