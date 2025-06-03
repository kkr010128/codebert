while 1:
    numbers = [i for i in raw_input()]
    if numbers[0] == '0': break
    print sum(map(int,numbers))