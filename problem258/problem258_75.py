N = int(input())

if N % 2 == 1:
    print(0)
else:
    n = 0
    i = 1
    while True:
        if N < 2*5**i:
            break
        n += (N // 5**i // 2)
        i += 1
    print(n)
