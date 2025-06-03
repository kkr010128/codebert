sum = 0
while(1):
    num = raw_input()
    if num == '0':
        break
    else:
        for i in range(len(num)):
            sum += int(num[i])
    print sum
    sum = 0