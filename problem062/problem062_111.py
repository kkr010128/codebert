while True:
    numbers = list(map(int,input()))
    if numbers[0] == 0:
        break
    print(sum(numbers))