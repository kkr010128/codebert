while True:
    (n, x) = [int(i) for i in input().split()]
    if n == x == 0:
        break

    dataset = []
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            for c in range(b + 1, n + 1):
                dataset.append([a,b,c])

    count = 0
    for data in dataset:
        if sum(data) == x:
            count += 1

    print(count)