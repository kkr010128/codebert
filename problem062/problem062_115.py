# Sum of Numbers

end = 0
while end == 0:
    number = list(input())
    if number == ["0"]:
        end += 1
    else:
        # print(number)
        digitTotal = 0
        for digit in number:
            digitTotal += int(digit)
        print(digitTotal)

