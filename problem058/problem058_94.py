while True:
    n, x = map(int, input().split())
    if (n == x == 0):
        break

    count = 0
    for a in range(1, x // 3):
        for b in range(a + 1, x // 2):
            for c in range(b + 1, n + 1):
                Sum = a + b + c
                if (Sum == x):
                    count += 1 
    print(count)