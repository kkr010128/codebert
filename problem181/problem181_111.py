K = int(input())

k = K - 1

numbers = {
    0: 1
}

while k > 0:
    k -= 1
    for i in range(len(numbers)):
        n = numbers[i]
        if n == 9:
            continue

        if abs(numbers.get(i - 1, n) - (n + 1)) <= 1 and abs(numbers.get(i + 1, n) - (n + 1)) <= 1:
            numbers[i] += 1
            j = i - 1
            while j >= 0:
                numbers[j] = max(numbers[j + 1] - 1, 0)
                j -= 1
            break
    else:
        for key in numbers.keys():
            numbers[key] = 0
        numbers[len(numbers)] = 1

print(''.join([str(numbers[i]) for i in range(len(numbers))])[::-1])
