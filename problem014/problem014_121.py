def bubble_sort(numbers, n):
    """bubble sort method

    Args:
        numbers: a list of numbers to be sorted by bubble sort
        n: len(list)

    Returns:
        sorted list
    """
    flag = True
    counter = 0
    while flag:
        flag = False
        for index in range(n - 1, 0, -1):
            if numbers[index] < numbers[index - 1]:
                numbers[index], numbers[index - 1] = numbers[index - 1], numbers[index]
                flag = True
                counter += 1
    return numbers, counter


n = int(raw_input())
numbers = [int(x) for x in raw_input().split()]
numbers, swapped_numbers = bubble_sort(numbers, n)

print(" ".join([str(x) for x in numbers]))
print(swapped_numbers)