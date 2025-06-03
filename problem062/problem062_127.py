while True:
    n = input()
    if n == '0':
        break
    print(sum(map(int, n)))