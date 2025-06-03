x = int(input())
i = 0
ganpon = 100
while True:
    if x > ganpon:
        ganpon += int(ganpon//100)
        i += 1
    else:
        print(i)
        break