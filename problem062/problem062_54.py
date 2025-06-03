while True:
    sum = 0
    input_str = input()
    if input_str == '0':
        break
    for chr in input_str:
        sum += int(chr)
    print(sum)

