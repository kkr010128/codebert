while True:
    n = list(input())
    if n[0] == '0':
        break
    sum = 0
    for i in n:
        sum += int(i)
    print(sum)