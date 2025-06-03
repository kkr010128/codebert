N = int(input())

if N % 2 != 0:
    print('0')
else:
    count = 0
    i = 1

    while True:
        dif = (N // 2) // (5 ** i)
        count += dif
        if dif == 0:
            break

        i += 1

    print(count)
