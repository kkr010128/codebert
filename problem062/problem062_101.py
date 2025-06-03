while 1:
    input = raw_input()
    num = len(input)
    input = int(input)
    
    if input == 0:
        break
        
    count = 0
    for i in range(num, 0, -1):
        value = int(input / 10**(i-1))
        input -= value * 10 ** (i-1)
        count += value

    print(count)