while True:
    [n, m] = [int(x) for x in raw_input().split()]
    if [n, m] == [0, 0]:
        break

    data = []
    for x in range(n, 2, -1):
        for y in range(x - 1, 1, -1):
            for z in range(y - 1, 0, -1):
                s = x + y + z
                if s < m:
                    break
                if s == m:
                    data.append(s)

    print(len(data))