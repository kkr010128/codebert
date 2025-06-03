str = input()
while int(str[0]):
    sum = 0
    for char in str:
        sum += int(char)
    print(sum)
    str = input()