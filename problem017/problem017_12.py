def insertion_sort(numbers, n, g):
    """insertion sort method
    (only elements whose distance is larger than g are the target)

    Args:
        numbers: list of elements to be sorted
        n: len(numbers)
        g: distance

    Returns:
        partially sorted list, counter
    """
    counter = 0
    copied_instance = []
    for data in numbers:
        copied_instance.append(data)

    for i in range(g, n):
        target = copied_instance[i]
        j = i - g
        while j >= 0 and target < copied_instance[j]:
            copied_instance[j + g] = copied_instance[j]
            j -= g
            counter += 1
        copied_instance[j + g] = target
    return copied_instance, counter


def shell_sort(numbers, n, key=lambda x: x):
    """shell sort method

    Args:
        numbers: list of elements to be sorted
        n: len(numbers)

    Returns:
        sorted numbers, used G, swapped number
    """
    counter = 0
    copied_instance = []
    for data in numbers:
        copied_instance.append(data)

    G = [1]
    g = 4
    while g < len(numbers):
        G.append(g)
        g = g * 3 + 1
    G = G[::-1]
    for g in G:
        copied_instance, num = insertion_sort(copied_instance, n, g)
        counter += num

    return copied_instance, G, counter


length = int(raw_input())
numbers = []
counter = 0
while counter < length:
    numbers.append(int(raw_input()))
    counter += 1

numbers, G, counter = shell_sort(numbers, length)
print(len(G))
print(" ".join([str(x) for x in G]))
print(counter)
for n in numbers:
    print(str(n))