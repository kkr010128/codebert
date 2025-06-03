while True:
    numbers = [int(i) for i in  list(input())]
    if len(numbers) == 1 and numbers[0] == 0:
        break
    print(sum(numbers))